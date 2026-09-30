from django.urls import path
from rest_framework.routers import DefaultRouter
from interacoes import views

urlpatterns = [
    path("", Teste.as_view(), name="index"),
]