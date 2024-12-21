# core/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.controlador_principal, name='controlador_principal'),
]
