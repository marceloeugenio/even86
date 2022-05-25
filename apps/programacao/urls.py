
from django.urls import path
from .views import ProgramacaoView
from django.views.generic.base import TemplateView

urlpatterns = [
    path('listar/', ProgramacaoView.as_view(), name='programacao_listar'),
]
