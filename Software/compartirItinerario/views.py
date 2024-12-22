# compartirItinerario/views.py

from django.shortcuts import render, redirect
from django.contrib import messages
from core.models import Viajero, Itinerario, ItinerarioCompartido

def compartir_itinerario(request, correo_viajero):
    if request.method == "GET":
        try:
            viajero = Viajero.objects.get(correo=correo_viajero)
        except Viajero.DoesNotExist:
            messages.error(request, "El viajero no existe.")
            return render(request, 'compartir.html', {'itinerarios': []})

        itinerarios = Itinerario.objects.filter(viajero=viajero)
        return render(request, 'compartir.html', {'itinerarios': itinerarios})

    elif request.method == "POST":
        itinerario_nombre = request.POST.get('itinerario_nombre')
        correo_receptor = request.POST.get('correo_destinatario')

        try:
            viajero = Viajero.objects.get(correo=correo_viajero)
            itinerario = Itinerario.objects.get(nombre=itinerario_nombre, viajero=viajero)

            # Crear una copia del itinerario en ItinerarioCompartido
            ItinerarioCompartido.compartir_itinerario(
                itinerario=itinerario,
                correo_emisor=correo_viajero,
                correo_receptor=correo_receptor
            )

            messages.success(request, f"El itinerario '{itinerario.nombre}' se ha compartido con {correo_receptor}.")
        except Viajero.DoesNotExist:
            messages.error(request, "El viajero no existe.")
        except Itinerario.DoesNotExist:
            messages.error(request, "El itinerario no existe.")
        except Exception as e:
            messages.error(request, f"Ocurrió un error: {str(e)}")

        return redirect('compartir_itinerario', correo_viajero=correo_viajero)

