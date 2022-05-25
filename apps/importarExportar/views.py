from django.views.generic import TemplateView


class ImpExpoView(TemplateView):
    template_name = "importar_exportar/listar.html"

    def get_context_data(self, **kwargs):
        context = super(ImpExpoView, self).get_context_data(**kwargs)
        return context
