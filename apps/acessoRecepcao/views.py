from django.shortcuts import render

from django.views.generic import (
    CreateView, TemplateView, UpdateView, FormView
)
class AcessoRecepcaoView(TemplateView):
    template_name = "acesso/recepcao.html"
  
    def get_context_data(self, **kwargs):
        context = super(AcessoRecepcaoView, self).get_context_data(**kwargs)
        return context