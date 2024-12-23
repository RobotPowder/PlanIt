
from django.shortcuts import render, redirect
from django.contrib import messages
from core.models import ItinerarioCompartido, Viajero, Itinerario

def recibir_itinerario(request, correo_viajero):
    if request.method == "GET":
        # Verificar si hay itinerarios compartidos con este correo
        itinerarios_compartidos = ItinerarioCompartido.objects.filter(receptor=correo_viajero)

        if not itinerarios_compartidos.exists():
            messages.error(request, "No tienes itinerarios compartidos.")
            return render(request, 'recibir.html', {'itinerarios': []})

        # Mostrar itinerarios compartidos al usuario
        return render(request, 'recibir.html', {'itinerarios': itinerarios_compartidos})

    elif request.method == "POST":
        # Obtener los datos del itinerario seleccionado
        itinerario_id = request.POST.get('itinerario_id')
        accion = request.POST.get('accion')

        try:
            itinerario_compartido = ItinerarioCompartido.objects.get(id=itinerario_id, receptor=correo_viajero)

            if accion == "aceptar":
                # Crear una copia del itinerario para el receptor
                receptor = Viajero.objects.get(correo=correo_viajero)
                Itinerario.objects.create(
                    viajero=receptor,
                    nombre=itinerario_compartido.itinerario.nombre,
                    fecha=itinerario_compartido.itinerario.fecha
                )
                messages.success(request, f"Has aceptado el itinerario '{itinerario_compartido.itinerario.nombre}'.")

            elif accion == "rechazar":
                # Solo muestra un mensaje de rechazo
                messages.info(request, f"Has rechazado el itinerario '{itinerario_compartido.itinerario.nombre}'.")

        except ItinerarioCompartido.DoesNotExist:
            messages.error(request, "No se encontró el itinerario compartido.")

        return redirect('recibir_itinerario', correo_viajero=correo_viajero)
