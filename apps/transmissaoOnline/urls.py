
from django.urls import path
from .views import TransmissaoOnlineView
from django.views.generic.base import TemplateView

urlpatterns = [
    path('listar/', TransmissaoOnlineView.as_view(), name='transmissao_online_listar'),
]
