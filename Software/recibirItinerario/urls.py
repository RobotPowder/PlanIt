from django.urls import path
from . import views

urlpatterns = [
    path('<str:correo_viajero>/', views.recibir_itinerario, name='recibir_itinerario'),
]
