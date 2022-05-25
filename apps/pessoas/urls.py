from django.urls import path, re_path

from .views import (PessoasAdicionarView, PessoasEditarView,
                    PessoasExcluirView, PessoasLerView, PessoasListView)

urlpatterns = [
    path("listar/", PessoasListView.as_view(), name="pessoas_list"),
    path("ler/<int:pk>/", PessoasLerView.as_view(), name="pessoas_ler"),
    path("adicionar/", PessoasAdicionarView.as_view(), name="pessoas_adicionar"),
    path("editar/<int:pk>/", PessoasEditarView.as_view(), name="pessoas_editar"),
    path("excluir/<int:pk>/", PessoasExcluirView.as_view(), name="pessoas_excluir"),
    re_path(
        r'^adicionar/(?P<success>[a-z]{7})/$',
        PessoasAdicionarView.as_view(),
        name="pessoas_adicionar",
    ),
]
