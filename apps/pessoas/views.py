from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from .forms import PessoasForm
from .models import Pessoas


# class PessoasListView( View):
class PessoasListView(LoginRequiredMixin, PermissionRequiredMixin, View):
    permission_required = "pessoas.list_pessoas"
    template_name = "pessoas/pessoas_list.html"

    def get(self, request, *args, **kwargs):
        context = {
            "object_list": Pessoas.objects.all(),
        }
        return render(request, self.template_name, context)


class PessoasLerView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    permission_required = "pessoas.view_pessoas"
    model = Pessoas

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["object"] = get_object_or_404(Pessoas, pk=self.kwargs["pk"])

        return context


class PessoasAdicionarView(CreateView):
    # class PessoasAdicionarView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    # permission_required = ('pessoas.add_pessoas')
    form_class = PessoasForm
    template_name = "pessoas/pessoas_form.html"
    success_url = "/pessoas/adicionar"

    def get(self, request, success=None):
        form = PessoasForm()
        # form.fields['ativ_fk_diario'].queryset = Diario.objects.filter(diar_fk_professor=request.session['sistema_usu_grupo_logado'], diar_ano_letivo=request.
        # session['sistema_ano_letivo'])
        context = {"success": success}
        return render(request, self.template_name, {"form": form, "context": context})

    def post(self, request, success=None, *args, **kwargs):

        form = PessoasForm(request.POST)

        if form.is_valid():
            usuario = get_object_or_404(get_user_model(), pk=request.user.id)
            aprendermais = form.save()
            # aprendermais.apma_fk_usuario_inclusao = usuario
            # aprendermais.apma_fk_empresa = get_object_or_404(Empresa, pk=request.session['sistema_empresa'])
            aprendermais.save()
            context = {"success": "success"}

            return HttpResponseRedirect(
                reverse_lazy("pessoas_adicionar", args=(context))
            )

        context = {"success": None}

        return render(request, self.template_name, {"form": form, "context": context})


class PessoasEditarView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = "pessoas.change_pessoas"
    model = Pessoas
    template_name = "pessoas/pessoas_update_form.html"
    form_class = PessoasForm
    success_url = reverse_lazy("pessoas_list")

    def get_form(self, form_class=None):
        if form_class is None:
            form_class = self.get_form_class()
        return form_class(**self.get_form_kwargs())

    def form_valid(self, form, *args, **kwargs):

        object = form.save(commit=False)
        if self.request.user:
            usuario = get_object_or_404(get_user_model(), pk=self.request.user.pk)
            object.apma_fk_usuario_alteracao = usuario
            object.save()

        # aprendermais = get_object_or_404(Aprendermais, pk=self.kwargs['pk'])
        # form.instance.user = self.request.user
        # form.save()

        messages.success(self.request, "Pessoa alterado com sucesso")
        return super().form_valid(form, *args, **kwargs)

    def form_invalid(self, form, *args, **kwargs):
        messages.error(self.request, "Erro ao cadastrar pessoa")
        return super().form_invalid(form, *args, **kwargs)


class PessoasExcluirView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    permission_required = "pessoas.delete_pessoas"
    model = Pessoas
    success_url = reverse_lazy("pessoas_list")
