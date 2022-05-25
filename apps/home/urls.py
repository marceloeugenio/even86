
from django.urls import path

from .views import (DashboardCertificadosView, DashboardInscricoesView,
                    HomeSiteView, get_inscricao, get_inscricao_por_categoria,
                    get_inscricao_por_mes)

urlpatterns = [
    path('', HomeSiteView.as_view()),
    path('', HomeSiteView.as_view(), name='home'),
    path('dashboard_inscricoes/', DashboardInscricoesView.as_view(),
         name='dashboard_inscricoes'),
    path('dashboard_certificados/', DashboardCertificadosView.as_view(),
         name='dashboard_certificados'),
    path('get_inscricao/', get_inscricao),
    path('get_inscricao_por_categoria/', get_inscricao_por_categoria),
    path('get_inscricao_por_mes/', get_inscricao_por_mes),
]
