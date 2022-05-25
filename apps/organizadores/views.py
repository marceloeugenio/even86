from django.shortcuts import render

from django.views.generic import (
    CreateView, TemplateView, UpdateView, FormView
)
class OrganizadoresView(TemplateView):
    template_name = "organizadores/listar.html"
  
    def get_context_data(self, **kwargs):
        context = super(OrganizadoresView, self).get_context_data(**kwargs)
        return context