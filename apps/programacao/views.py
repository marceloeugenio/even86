from django.shortcuts import render

from django.views.generic import (
    CreateView, TemplateView, UpdateView, FormView
)
class ProgramacaoView(TemplateView):
    template_name = "programacao/listar.html"
  
    def get_context_data(self, **kwargs):
        context = super(ProgramacaoView, self).get_context_data(**kwargs)
        return context