# compartirItinerario/views.py
from django.shortcuts import render, redirect
from django.contrib import messages
from core.models import Itinerario, Viajero, ItinerarioCompartido

def compartir_itinerario(request):
    if request.method == "GET":
        # 1. Obtener el viajero mediante su correo (supongamos que el correo se obtiene de la autenticación o como parámetro)
        correo_viajero = "viajero@example.com"  # Ejemplo, puedes reemplazarlo con request.user.email si usas autenticación
        try:
            viajero = Viajero.objects.get(correo=correo_viajero)
        except Viajero.DoesNotExist:
            messages.error(request, "El viajero no existe.")
            return render(request, 'compartir.html', {'itinerarios': []})  # Renderiza la misma página con error

        # 2. Obtener los itinerarios asociados al viajero
        itinerarios = Itinerario.objects.filter(viajero=viajero)
        return render(request, 'compartir.html', {'itinerarios': itinerarios})

    elif request.method == "POST":
        # 3. Procesar el formulario enviado
        correo_viajero = "viajero@example.com"  # Supongamos que viene del usuario autenticado
        itinerario_nombre = request.POST.get('itinerario_nombre')  # Recibe el nombre del itinerario
        correo_destinatario = request.POST.get('correo_destinatario')  # Recibe el correo del destinatario

        if itinerario_nombre and correo_destinatario:
            try:
                # Buscar el viajero por su correo
                viajero = Viajero.objects.get(correo=correo_viajero)

                # Buscar el itinerario por su nombre y viajero
                itinerario = Itinerario.objects.get(nombre=itinerario_nombre, viajero=viajero)

                # Crear el itinerario compartido
                ItinerarioCompartido.compartir_itinerario(itinerario, correo_destinatario)

                # Mostrar un mensaje de éxito
                messages.success(request, f"Se ha compartido el itinerario '{itinerario.nombre}' con {correo_destinatario}.")
                return redirect('compartir_itinerario')
            except Viajero.DoesNotExist:
                messages.error(request, "El viajero no existe.")
            except Itinerario.DoesNotExist:
                messages.error(request, "El itinerario no existe para este viajero.")
        else:
            messages.error(request, "Por favor, selecciona un itinerario y proporciona un correo válido.")

        return redirect('compartir_itinerario')

