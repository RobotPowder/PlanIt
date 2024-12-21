from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def controlador_principal(request):
    """
    Controlador principal que permite seleccionar entre las apps crearItinerario y visualizarItinerario.
    """
    return render(request, 'core/templates/controlador_principal.html')  # Renderiza la vista correspondiente


