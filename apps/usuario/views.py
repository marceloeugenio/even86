from django.shortcuts import render

from django.views.generic import (
    CreateView, TemplateView, UpdateView, FormView
)
class UsuarioPerfilView(TemplateView):
    template_name = "usuario/perfil.html"
  
    def get_context_data(self, **kwargs):
        context = super(UsuarioPerfilView, self).get_context_data(**kwargs)
        return context