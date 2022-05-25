
from django.urls import path
from .views import OrganizadoresView
from django.views.generic.base import TemplateView

urlpatterns = [
    path('listar/', OrganizadoresView.as_view(), name='organizadores_listar'),
]
