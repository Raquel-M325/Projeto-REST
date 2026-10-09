from django.urls import path
from .views import ClienteViewSet

app_name = "cliente"

urlpatterns = [
    # PUBLICADORES
    path(
        "publicadores/",
        ClienteViewSet.as_view({
            "get": "listar_publicadores",
            "post": "criar_publicador",
        }),
        name="publicadores",
    ),
    path(
        "publicadores/<int:pk>/",
        ClienteViewSet.as_view({
            "get": "detalhar_publicador",
            "put": "editar_publicador",
            "patch": "atualizar_parcial_publicador",
            "delete": "excluir_publicador",
        }),
        name="publicador-detalhe",
    ),

    # PUBLICAÇÕES
    path(
        "publicacoes/",
        ClienteViewSet.as_view({
            "get": "listar_publicacoes",
            "post": "criar_publicacao",
        }),
        name="publicacoes",
    ),
    path(
        "publicacoes/<int:pk>/",
        ClienteViewSet.as_view({
            "get": "detalhar_publicacao",
            "put": "editar_publicacao",
            "patch": "atualizar_parcial_publicacao",
            "delete": "excluir_publicacao",
        }),
        name="publicacao-detalhe",
    ),

    # AVALIADORES
    path(
        "avaliadores/",
        ClienteViewSet.as_view({
            "get": "listar_avaliadores",
            "post": "criar_avaliador",
        }),
        name="avaliadores",
    ),
    path(
        "avaliadores/<int:pk>/",
        ClienteViewSet.as_view({
            "get": "detalhar_avaliador",
            "put": "editar_avaliador",
            "patch": "atualizar_parcial_avaliador",
            "delete": "excluir_avaliador",
        }),
        name="avaliador-detalhe",
    ),

    # AVALIAÇÕES
    path(
        "avaliacoes/",
        ClienteViewSet.as_view({
            "get": "listar_avaliacoes",
            "post": "criar_avaliacao",
        }),
        name="avaliacoes",
    ),
    path(
        "avaliacoes/<int:pk>/",
        ClienteViewSet.as_view({
            "get": "detalhar_avaliacao",
            "put": "editar_avaliacao",
            "patch": "atualizar_parcial_avaliacao",
            "delete": "excluir_avaliacao",
        }),
        name="avaliacao-detalhe",
    ),
]

