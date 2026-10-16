from django.urls import path
from django.shortcuts import render
from .services.gateway import GatewayProxyView, NotasPublicasView

app_name = "gateway"

urlpatterns = [
    path("", lambda request: render(request, "app/index.html"), name="pagina_inicial"),
    path("v1/notas/", NotasPublicasView.as_view(), name="notas-publicas"),
    path("v1/<str:recurso>/", GatewayProxyView.as_view(), name="gateway-list"),
    path("v1/<str:recurso>/<int:pk>/", GatewayProxyView.as_view(), name="gateway-detail"),
]
