from django.shortcuts import render

from django.views.generic import (
    CreateView, TemplateView, UpdateView, FormView
)
class EventoView(TemplateView):
    template_name = "evento/listar.html"
  
    def get_context_data(self, **kwargs):
        context = super(EventoView, self).get_context_data(**kwargs)
        return context