# compartirItinerario/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('compartir/', views.compartir_itinerario, name='compartir_itinerario'),
]
