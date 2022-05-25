
from django.urls import path
from .views import UsuarioPerfilView
from django.views.generic.base import TemplateView

urlpatterns = [
    path('perfil/', UsuarioPerfilView.as_view(), name='usuario_perfil'),
]
