
from django.urls import path
from .views import SubmissoesControleView
from django.views.generic.base import TemplateView

urlpatterns = [
    path('listar/', SubmissoesControleView.as_view(), name='submissoes_controle_listar'),
]
