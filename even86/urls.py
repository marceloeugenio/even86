from apps.acessoRecepcao import urls as acessoRecepcao_urls
from apps.ajuda import urls as ajuda_urls
from apps.atividade import urls as atividade_urls
from apps.credenciamento import urls as credenciamento_urls
from apps.evento import urls as evento_urls
from apps.feedback import urls as feedback_urls
from apps.geradorCertificados import urls as geradorCertificados_urls
from apps.geradorCracha import urls as geradorCracha_urls
from apps.home import urls as home_urls
from apps.importarExportar import urls as importarExportar_urls
from apps.inscricao import urls as inscricao_urls
from apps.organizadores import urls as organizadores_urls
from apps.pessoas import urls as pessoas_urls
from apps.programacao import urls as programacao_urls
from apps.submissoes import urls as submissoes_urls
from apps.submissoesControle import urls as submissoesControle_urls
from apps.transmissaoOnline import urls as transmissaoOnline_urls
from apps.usuario import urls as usuario_urls
from apps.validacaoCertificado import urls as validacaoCertificado_urls
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.urls import include, path

urlpatterns = [
    path("accounts/", include("django.contrib.auth.urls")),
    path("login/", auth_views.LoginView.as_view(), name="login"),
    path("", include(home_urls)),
    path("acesso/", include(acessoRecepcao_urls)),
    path("ajuda/", include(ajuda_urls)),
    path("atividade/", include(atividade_urls)),
    path("credenciamento/", include(credenciamento_urls)),
    path("evento/", include(evento_urls)),
    path("feedback/", include(feedback_urls)),
    path("gerador_certificados/", include(geradorCertificados_urls)),
    path("gerador_cracha/", include(geradorCracha_urls)),
    path("importar_exportar/", include(importarExportar_urls)),
    path("inscricao/", include(inscricao_urls)),
    path("pessoas/", include(pessoas_urls)),
    path("programacao/", include(programacao_urls)),
    path("submissoes/", include(submissoes_urls)),
    path("submissoes_controle/", include(submissoesControle_urls)),
    path("transmissao_online/", include(transmissaoOnline_urls)),
    path("usuario/", include(usuario_urls)),
    path("transmissao_online/", include(transmissaoOnline_urls)),
    path("validacao_certificado/", include(validacaoCertificado_urls)),
    path("organizadores/", include(organizadores_urls)),
    path(
        "password-reset/",
        auth_views.PasswordResetView.as_view(
            template_name="conta/password_reset_form.html",
            html_email_template_name="conta/password_reset_html_email.html",
            email_template_name="conta/password_reset_confirm.html",
            subject_template_name="conta/password_reset_subject.txt",
        ),
        name="password_reset",
    ),
    path(
        "password-reset/done/",
        auth_views.PasswordResetDoneView.as_view(
            template_name="conta/password_reset_done.html"
        ),
        name="password_reset_done",
    ),
    path(
        "password-reset-complete/",
        auth_views.PasswordResetCompleteView.as_view(
            template_name="conta/password_reset_complete.html"
        ),
        name="password_reset_complete",
    ),
    path(
        "password-reset-confirm/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(
            template_name="conta/password_reset_confirm.html"
        ),
        name="password_reset_confirm",
    ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
