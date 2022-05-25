
from django.urls import path
from .views import ValidacaoCertificadoView
from django.views.generic.base import TemplateView

urlpatterns = [
    path('listar/', ValidacaoCertificadoView.as_view(), name='validacao_certificado_listar'),
]
