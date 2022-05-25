from django.urls import path

from .views import GeradorCrachaView

urlpatterns = [
    path("listar/", GeradorCrachaView.as_view(), name="gerador_cracha_listar")
]
