from django.urls import path

from .views import AtividadeView

urlpatterns = [
    path("listar/", AtividadeView.as_view(), name="atividade_listar"),
]
