from interacoes.views import AvaliacaoViewSet
from gerencia.views import PublicacaoViewSet

from .permissions import (
    LeituraAutenticadaEscritaAvaliador,
    LeituraAutenticadaEscritaPublicador,
)


class GatewayAvaliacaoViewSet(AvaliacaoViewSet):
    permission_classes = [LeituraAutenticadaEscritaAvaliador]


class GatewayPublicacaoViewSet(PublicacaoViewSet):
    permission_classes = [LeituraAutenticadaEscritaPublicador]