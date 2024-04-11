# Generated by Django 2.2 on 2021-04-09 09:18

from django.db import migrations


def methode_paiement_fraction(apps, schema_editor):
    # We can't import the Person model directly as it may be a newer
    # version than this migration expects. We use the historical version.
    Methode = apps.get_model('APIcashless', 'Methode')
    Configuration = apps.get_model('APIcashless', 'Configuration')
    Articles = apps.get_model('APIcashless', 'Articles')
    MoyenPaiement = apps.get_model('APIcashless', 'MoyenPaiement')

    # import ipdb; ipdb.set_trace()

    configuration = Configuration.objects.get_or_create()[0]

    paiement_fractionne = Methode.objects.get_or_create(name="PaiementFractionne")[0]

    moyen_de_paiement_fractionne = MoyenPaiement.objects.get_or_create(name="Paiement Fractionné")[0]

    configuration.methode_paiement_fractionne = paiement_fractionne
    configuration.moyen_paiement_fractionne = moyen_de_paiement_fractionne
    configuration.save()


def reverse(apps, schema_editor):
    Methode = apps.get_model('APIcashless', 'Methode')
    Articles = apps.get_model('APIcashless', 'Articles')
    MoyenPaiement = apps.get_model('APIcashless', 'MoyenPaiement')

    try:
        art = Articles.objects.get_or_create(name="Paiement Fractionné")
        art.delete()
    except:
        pass

    try :
        moyen_de_paiement_fractionne = MoyenPaiement.objects.get(name="Paiement Fractionné")
        moyen_de_paiement_fractionne.delete()
    except:
        pass

    try:
        paiement_fractionne = Methode.objects.get(name="PaiementFractionne")
        paiement_fractionne.delete()
    except:
        pass

class Migration(migrations.Migration):

    dependencies = [
        ('APIcashless', '0018_auto_20210409_1154'),
    ]

    operations = [
        migrations.RunPython(methode_paiement_fraction, reverse),
    ]