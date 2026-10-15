
from django.urls import path
from django.shortcuts import render

urlpatterns = [
    path('', lambda request: render(request, 'app/index.html'), name='pagina_inicial'),
]