from django.shortcuts import render, redirect, get_object_or_404
from .forms import ActividadForm
from core.models import Itinerario, Actividad


def ver_itinerario(request, itinerario_id):
    itinerario = get_object_or_404(Itinerario, id=itinerario_id)
    actividades = itinerario.actividades.all().order_by('horario')  # Ordena por el horario

    return render(request, 'ver_itinerario.html', {'itinerario': itinerario, 'actividades': actividades,})


# Agregar actividad (sin login_required)
def agregar_actividad(request, itinerario_id):
    itinerario = get_object_or_404(Itinerario, id=itinerario_id)

    if request.method == "POST":
        form = ActividadForm(request.POST)
        if form.is_valid():
            actividad = form.save(commit=False)
            actividad.itinerario = itinerario
            actividad.save()
            return redirect("ver_itinerario", itinerario_id=itinerario.id)
    else:
        form = ActividadForm()

    return render(request, "agregar_actividad.html", {"form": form, "itinerario": itinerario})


# Modificar actividad (sin login_required)
def modificar_actividad(request, actividad_id):
    actividad = get_object_or_404(Actividad, id=actividad_id)
    itinerario_id = actividad.itinerario.id  # Obtiene el itinerario asociado a la actividad

    if request.method == "POST":
        form = ActividadForm(request.POST, instance=actividad)
        if form.is_valid():
            form.save()
            return redirect("ver_itinerario", itinerario_id=itinerario_id)  # Cambia a la vista que muestra el itinerario.
    else:
        form = ActividadForm(instance=actividad)

    return render(request, "modificar_actividad.html", {"form": form, "actividad": actividad})


# Eliminar actividad (sin login_required)
def eliminar_actividad(request, actividad_id):
    actividad = get_object_or_404(Actividad, id=actividad_id)
    itinerario_id = actividad.itinerario.id  # Guarda el itinerario para redirigir después.
    
    if request.method == "POST":
        actividad.delete()
        return redirect("ver_itinerario", itinerario_id=itinerario_id)  # Cambia a la vista que muestra el itinerario.
    
    return render(request, "eliminar_actividad.html", {"actividad": actividad})
