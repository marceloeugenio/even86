from django.urls import path

from .views import AjudaView

urlpatterns = [
    path("informacoes/", AjudaView.as_view(), name="ajuda_informacoes"),
]
