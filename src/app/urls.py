from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (
    GatewayAvaliacaoViewSet,
    GatewayPublicacaoViewSet,
)

app_name = "gateway"

router = DefaultRouter()
router.register(
    "avaliacoes",
    GatewayAvaliacaoViewSet,
    basename="gateway-avaliacao",
)
router.register(
    "publicacoes",
    GatewayPublicacaoViewSet,
    basename="gateway-publicacao",
)

urlpatterns = [
    path("", include(router.urls)),
]