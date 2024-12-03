import logging
from lib2to3.fixes.fix_input import context

from django.http import HttpRequest
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request

from APIcashless.models import CommandeSauvegarde, CarteCashless, CarteMaitresse, ArticleVendu, MoyenPaiement
from administration.adminroot import ArticlesAdmin
from webview.serializers import debut_fin_journee, CommandeSerializer
from django.core.paginator import Paginator

logger = logging.getLogger(__name__)


class Sales(viewsets.ViewSet):
    authentication_classes = [SessionAuthentication, ]
    permission_classes = [IsAuthenticated, ]

    def list(self, request: Request):

        # ex : wv/allOrders?oldest_first=True
        order = '-datetime'
        authorized_management_mode = False

        oldest_first = False
        if request.GET.get('oldest_first'):
            if request.GET.get('oldest_first').lower().capitalize() == 'True':
                oldest_first = True

        if request.GET.get('authorized_management_mode') is not None:
            if request.GET.get('authorized_management_mode').lower().capitalize() == 'True':
                authorized_management_mode = True

        if oldest_first:
            order = 'datetime'

        debut_journee, fin_journee = debut_fin_journee()
        # Ex objet :
        # commands_today = CommandeSauvegarde.objects.filter(
        #     archive=False,
        #     datetime__gte=debut_journee
        # ).order_by(order).distinct()

        commands_today = {}
        articles_vendus = ArticleVendu.objects.filter(
            date_time__gte=debut_journee
        )
        paginator = Paginator(articles_vendus, 20)
        page_number = request.GET.get('page')

        for article in articles_vendus:
            if commands_today.get(article.commande) == None:
                commands_today[article.commande] = {
                    'articles': [article],
                    'total': article.qty * article.prix
                }
            else:
                commands_today[article.commande]['articles'].append(article)
                commands_today[article.commande]['total'] = commands_today[article.commande]['total'] + (article.qty * article.prix)

        context = {
            'commands_today': commands_today,
            'authorized_management_mode': authorized_management_mode,
            'oldest_first': oldest_first,
            'moyens_paiement': MoyenPaiement.objects.filter(categorie__in=[MoyenPaiement.CASH,MoyenPaiement.CHEQUE,MoyenPaiement.CREDIT_CARD_NOFED]),
            }

        return render(request, "sales/list.html", context)

    @action(detail=False, methods=['POST'])
    def change_payment_method(self, request):
        print('-> url = change_payment_method !')

        mp = MoyenPaiement.objects.get(pk=request.data['PaymentMethod_pk'])
        ArticleVendu.objects.filter(commande=request.data['commande_pk']).update(
            moyen_paiement=mp
        )

        context = {}
        # Todo : Retourner le template de la ligne article
        return render(request, "sales/list.html", context)

class Membership(viewsets.ViewSet):
    authentication_classes = [SessionAuthentication, ]
    permission_classes = [IsAuthenticated, ]

    def retrieve(self, request: HttpRequest, pk):
        logger.info(pk)
        pass
