from django.urls import path

from .views import CredenciamentoView

urlpatterns = [
    path("listar/", CredenciamentoView.as_view(), name="credenciamento_listar")
]
