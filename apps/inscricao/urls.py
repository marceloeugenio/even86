
from django.urls import path
from .views import InscricaoView
from django.views.generic.base import TemplateView

urlpatterns = [
    path('listar/', InscricaoView.as_view(), name='inscricao_listar'),
]
