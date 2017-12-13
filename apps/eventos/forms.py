from django import forms

from .models import Evento


class FormEvento(forms.ModelForm):
    class Meta:
        model = Evento
        fields = ('titulo', 'descripcion',)
