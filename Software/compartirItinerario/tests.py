# compartirItinerario/tests.py
from django.test import TestCase
from django.urls import reverse  # Para construir URLs basadas en sus nombres
from core.models import Viajero, Itinerario

class CompartirItinerarioTests(TestCase):

    def setUp(self):
        """
        Configura datos iniciales para las pruebas.
        """
        # Crear un viajero
        self.viajero = Viajero.objects.create(
            nombre="Carlos",
            correo="carlos@example.com",
            contraseña="123456"
        )

        # Crear itinerarios para el viajero
        Itinerario.objects.create(viajero=self.viajero, nombre="Viaje a la playa", fecha="2024-12-25")
        Itinerario.objects.create(viajero=self.viajero, nombre="Viaje a la montaña", fecha="2024-12-30")

    def test_compartir_itinerario_get(self):
        """
        Prueba la respuesta de la vista 'compartir_itinerario' con el método GET.
        """
        # Simula una solicitud GET a la URL de compartir itinerario
        response = self.client.get(reverse('compartir_itinerario'))

        # Verifica que la respuesta sea exitosa (HTTP 200)
        self.assertEqual(response.status_code, 200)

        # Verifica que los itinerarios creados aparecen en la respuesta
        self.assertContains(response, "Viaje a la playa")
        self.assertContains(response, "Viaje a la montaña")

    def test_compartir_itinerario_viajero_no_existe(self):
        """
        Prueba que se maneje correctamente el caso en el que no existe el viajero.
        """
        # Cambia temporalmente el correo del viajero (simulando un usuario inexistente)
        response = self.client.get(reverse('compartir_itinerario'))
        self.assertContains(response, "No se encontró un viajero con el correo especificado.")
