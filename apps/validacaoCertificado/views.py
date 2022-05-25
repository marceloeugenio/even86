from django.shortcuts import render

from django.views.generic import (
    CreateView, TemplateView, UpdateView, FormView
)
class ValidacaoCertificadoView(TemplateView):
    template_name = "validacao_certificado/listar.html"
  
    def get_context_data(self, **kwargs):
        context = super(ValueError, self).get_context_data(**kwargs)
        return context