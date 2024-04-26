import base64
import requests
from django.conf import settings
from django.utils import timezone
from rest_framework_api_key.models import APIKey

from APIcashless.custom_utils import jsonb64decode, dict_to_b64_utf8, dict_to_b64
from APIcashless.models import Configuration


import logging

from fedow_connect.tasks import after_handshake
from fedow_connect.utils import sign_message, verify_signature, data_to_b64

logger = logging.getLogger(__name__)



def handshake(config: Configuration, first_handshake=False):
    # Le handshake se lance lorsqu'une clé FEDOW est entré dans le menu de configuration
    # On récupère la clé publique de cette instance LaBoutik.
    # Si elle n'existe pas, la fonction la génère
    string_connect = config.string_connect
    ip_cashless = config.ip_cashless
    get_public_pem = config.get_public_pem()
    dokos_id = config.dokos_id

    decoded_data = None
    try:
        # La string est encodée en base64, on la décode
        # Récupération de l'adresse, de la clé api temporaire,
        # et de l'uuid correspondant à lieux qui a fait la demande de connection au FEDOW
        decoded_data = jsonb64decode(string_connect)

    except Exception as e:
        # Pour le mode test et dev', on va aller chercher une clé FEDOW sur le serveur de test
        if settings.DEBUG:
            session = requests.Session()
            name_enc = data_to_b64({'name': f'{config.structure}'})
            url = f'https://fedow.tibillet.localhost/get_new_place_token_for_test/{name_enc.decode("utf8")}/'
            request = session.get(url, verify=False, data={'name':f'{config.structure}'}, timeout=1)
            if request.status_code != 200:
                raise Exception("Erreur de connexion au serveur de test")
            string_connect = request.json().get('encoded_data')
            decoded_data = jsonb64decode(string_connect)

    if not decoded_data :
        raise Exception(f"Erreur decoded_data : None")

    fedow_domain = decoded_data['domain']
    fedow_place_uuid = decoded_data['uuid']
    fedow_key = decoded_data['temp_key']
    # Création de la clé API pour cette instance serveur LaBoutik
    api_key, key = APIKey.objects.create_key(name="fedow_key")

    # Toutes les infos sont ok pour le handshake, on renvoie la clé API et la clé publique RSA
    # Dictionnaire de réponse. On renvoie l'uuid avec la signature de fedow
    handshake_data = {
        "fedow_place_uuid": f"{fedow_place_uuid}",
        "cashless_ip": f"{ip_cashless}",
        "cashless_url": f"{settings.CASHLESS_URL}",
        "cashless_admin_apikey": f"{key}",
        "cashless_rsa_pub_key": f"{get_public_pem}",
        "dokos_id": f"{dokos_id}",
    }

    # Signature du dictionnaire pour s'assurer que le FEDOW utilise bien la même méthode de signature
    # car il devra la valider pour continuer le handshake.
    signature = sign_message(
        dict_to_b64(handshake_data),
        config.get_private_key()).decode('utf-8')

    # Ici, on s'auto vérifie :
    if not verify_signature(config.get_public_key(),
                            dict_to_b64(handshake_data),
                            signature):
        raise Exception("Erreur de signature")

    # Envoie de la requete à FEDOW : Dictionnaire + signature
    session = requests.Session()
    request_fedow = session.post(
        f"https://{fedow_domain}/place/handshake/",
        headers={
            "Authorization": f"Api-Key {fedow_key}",
            "Signature": f"{signature}"
        },
        data=handshake_data,
        verify=bool(not settings.DEBUG),
    )
    session.close()

    # Le retour du FEDOW est un code 202 si tout est ok
    # Handshake ok, on décode la réponse
    if request_fedow.status_code == 202:
        decoded_return_handshake = jsonb64decode(request_fedow.content)
        place_admin_apikey = decoded_return_handshake.get('place_admin_apikey')
        url_onboard = decoded_return_handshake.get('url_onboard')
        place_wallet_public_pem = decoded_return_handshake.get('place_wallet_public_pem')
        place_wallet_uuid = decoded_return_handshake.get('place_wallet_uuid')

        if key and url_onboard:
            # on va faire le after_handshake a la main
            if first_handshake:
                after_handshake.delay()

            return {
                'place_admin_apikey': place_admin_apikey,
                'place_wallet_public_pem': place_wallet_public_pem,
                'fedow_place_wallet_uuid': place_wallet_uuid,
                'url_onboard': url_onboard,
                'fedow_domain': fedow_domain,
                'fedow_place_uuid': fedow_place_uuid,
            }


    # Raise erreur si le code n'est pas 202
    logger.error(f"{timezone.localdate()} - erreur handkshake : {request_fedow.status_code} {request_fedow.content}")
    raise Exception(f"Erreur de handshake : {request_fedow.status_code} {request_fedow.content}")