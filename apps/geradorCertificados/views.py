from django.views.generic import TemplateView


class GerCertView(TemplateView):
    template_name = "gerador_certificados/listar.html"

    def get_context_data(self, **kwargs):
        context = super(GerCertView, self).get_context_data(**kwargs)
        return context
