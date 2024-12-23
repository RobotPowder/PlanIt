from django import forms
from .models import Actividad
from datetime import time

class ActividadForm(forms.ModelForm):
    HORARIOS = [(time(hour=h), f"{h:02d}:00 - {h + 1:02d}:00") for h in range(0, 24)]

    horario = forms.ChoiceField(choices=HORARIOS, label="Horario")

    class Meta:
        model = Actividad
        fields = ["horario", "nombre", "destino"]

    def clean_horario(self):
        horario = self.cleaned_data["horario"]
        return time.fromisoformat(horario)  # Convierte de string a objeto `time`
