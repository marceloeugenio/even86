from django.shortcuts import render

from django.views.generic import (
    CreateView, TemplateView, UpdateView, FormView
)
class AjudaView(TemplateView):
    template_name = "ajuda/informacoes.html"
  
    def get_context_data(self, **kwargs):
        context = super(AjudaView, self).get_context_data(**kwargs)
        return context