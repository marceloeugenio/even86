import random

from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import CreateView, FormView, TemplateView, UpdateView
from matplotlib.style import context
from rest_framework.views import APIView


class HomeSiteView(TemplateView):
    template_name = "home/site.html"

    def get_context_data(self, **kwargs):
        context = super(HomeSiteView, self).get_context_data(**kwargs)
        return context


class DashboardInscricoesView(TemplateView):
    template_name = "home/dashboard1.html"

    def get_context_data(self, **kwargs):
        context = super(DashboardInscricoesView,
                        self).get_context_data(**kwargs)
        return context


class DashboardCertificadosView(TemplateView):
    template_name = "home/dashboard2.html"

    def get_context_data(self, **kwargs):
        context = super(DashboardCertificadosView,
                        self).get_context_data(**kwargs)
        return context


def get_inscricao(request):
    context = {'confirmadas': random.randint(
        10, 100), 'canceladas': random.randint(10, 100), 'vagas': '40'}
    return render(request, 'home/partes/inscricao.html', context)


def get_inscricao_por_categoria(request):
    # context = {'inscricoes':random.randint(10,100), 'canceladas':random.randint(10,100), 'vagas':'40'}
    return render(request, 'home/partes/inscricao_por_categoria.html')


def get_inscricao_por_mes(request):
    # context = {'inscricoes':random.randint(10,100), 'canceladas':random.randint(10,100), 'vagas':'40'}
    return render(request, 'home/partes/inscricao_por_mes.html')
