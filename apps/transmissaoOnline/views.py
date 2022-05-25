from django.shortcuts import render

from django.views.generic import (
    CreateView, TemplateView, UpdateView, FormView
)
class TransmissaoOnlineView(TemplateView):
    template_name = "transmissao_online/listar.html"
  
    def get_context_data(self, **kwargs):
        context = super(TransmissaoOnlineView, self).get_context_data(**kwargs)
        return context