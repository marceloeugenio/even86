from django.urls import path

from .views import ImpExpoView

urlpatterns = [path("listar/", ImpExpoView.as_view(),
                    name="importar_exportar_listar")]
