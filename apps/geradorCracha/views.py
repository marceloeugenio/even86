from django.shortcuts import render

from django.views.generic import (
    CreateView, TemplateView, UpdateView, FormView
)
class GeradorCrachaView(TemplateView):
    template_name = "gerador_cracha/listar.html"
  
    def get_context_data(self, **kwargs):
        context = super(GeradorCrachaView, self).get_context_data(**kwargs)
        return context