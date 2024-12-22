from django.db import models

# Create your models here.
class Viajero(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)
    contraseña = models.CharField(max_length=100)

class Itinerario(models.Model):
    viajero = models.ForeignKey(Viajero, on_delete=models.CASCADE, related_name="itinerarios")
    nombre = models.CharField(max_length=100)
    fecha = models.DateField()
    @staticmethod
    def solicitar_itinerarios_viajero(viajero_id):
        """Devuelve todos los itinerarios de un viajero por su ID."""
        return Itinerario.objects.filter(viajero_id=viajero_id)

class Destino(models.Model):
    pais = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=100)
    direccion = models.TextField()

class Actividad(models.Model):
    horario = models.TimeField()
    nombre = models.CharField(max_length=100)
    destino = models.ForeignKey(Destino, on_delete=models.CASCADE, related_name="actividades")
    itinerario = models.ForeignKey(Itinerario, on_delete=models.CASCADE, related_name="actividades")

class ItinerarioCompartido(models.Model):
    itinerario = models.OneToOneField(Itinerario, on_delete=models.CASCADE, related_name="itinerario_compartido")
    emisor = models.EmailField()
    receptor = models.EmailField()

    @staticmethod
    def compartir_itinerario(itinerario, correo_emisor, correo_receptor):
        """
        Crea una nueva relación de itinerario compartido.
        """
        return ItinerarioCompartido.objects.create(
            itinerario=itinerario,
            emisor=correo_emisor,
            receptor=correo_receptor
        )
