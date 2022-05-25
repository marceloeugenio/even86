from django.urls import path

from .views import EventoView

urlpatterns = [
    path("listar/", EventoView.as_view(), name="evento_listar"),
]
