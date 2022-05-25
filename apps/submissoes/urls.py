
from django.urls import path
from .views import SubmissoesView
from django.views.generic.base import TemplateView

urlpatterns = [
    path('listar/', SubmissoesView.as_view(), name='submissoes_listar'),
]
