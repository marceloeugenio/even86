from django.shortcuts import render

from django.views.generic import (
    CreateView, TemplateView, UpdateView, FormView
)
class AtividadeView(TemplateView):
    template_name = "atividade/index.html"
  
    def get_context_data(self, **kwargs):
        context = super(AtividadeView, self).get_context_data(**kwargs)
        return context