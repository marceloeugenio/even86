from django.shortcuts import render

from django.views.generic import (
    CreateView, TemplateView, UpdateView, FormView
)
class SubmissoesView(TemplateView):
    template_name = "submissoes/listar.html"
  
    def get_context_data(self, **kwargs):
        context = super(SubmissoesView, self).get_context_data(**kwargs)
        return context