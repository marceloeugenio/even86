from django.urls import path

from .views import GerCertView

urlpatterns = [path("listar/", GerCertView.as_view(),
                    name="gerador_certificados_listar")]
