from django.shortcuts import render

from django.views.generic import (
    CreateView, TemplateView, UpdateView, FormView
)
class SubmissoesControleView(TemplateView):
    template_name = "submissoes_controle/listar.html"
  
    def get_context_data(self, **kwargs):
        context = super(SubmissoesControleView, self).get_context_data(**kwargs)
        return context