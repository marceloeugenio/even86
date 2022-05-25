from django.shortcuts import render

from django.views.generic import (
    CreateView, TemplateView, UpdateView, FormView
)
class InscricaoView(TemplateView):
    template_name = "inscricao/listar.html"
  
    def get_context_data(self, **kwargs):
        context = super(InscricaoView, self).get_context_data(**kwargs)
        return context