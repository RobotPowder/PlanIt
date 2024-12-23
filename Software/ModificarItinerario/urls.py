from django.urls import path
from . import views

urlpatterns = [
    path('itinerario/<int:itinerario_id>/', views.ver_itinerario, name='ver_itinerario'),
    path('agregar/<int:itinerario_id>/', views.agregar_actividad, name='agregar_actividad'),
    path('modificar/<int:actividad_id>/', views.modificar_actividad, name='modificar_actividad'),
    path('eliminar/<int:actividad_id>/', views.eliminar_actividad, name='eliminar_actividad'),
]
