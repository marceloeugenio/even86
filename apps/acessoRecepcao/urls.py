from django.urls import path

from .views import AcessoRecepcaoView

urlpatterns = [
    path("recepcao/", AcessoRecepcaoView.as_view(), name="acesso_recepcao"),
]
