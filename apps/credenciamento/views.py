from django.shortcuts import render

from django.views.generic import (
    CreateView, TemplateView, UpdateView, FormView
)
class CredenciamentoView(TemplateView):
    template_name = "credenciamento/listar.html"
  
    def get_context_data(self, **kwargs):
        context = super(CredenciamentoView, self).get_context_data(**kwargs)
        return context