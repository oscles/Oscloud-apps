from django import forms

from .models import Cliente


class FormCliente(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = (
            'nombre',
            'apellido',
            'telefono',
            'direccion',
            'email',
            'tipo',
        )

        widgets = {
            'nombre': forms.TextInput(
                attrs={'class': 'form-control',
                       'placeholder':'Ej. William '}
            ),
            'apellido': forms.TextInput(
                attrs={'class': 'form-control',
                       'placeholder':'Ej. Meza Peralta'}
            ),
            'telefono': forms.TextInput(
                attrs={'class': 'form-control',
                       'placeholder':'Ej. 300 546 2345'}
            ),
            'direccion': forms.TextInput(
                attrs={'class': 'form-control',
                       'placeholder':'Av. La Cordialidad Cr 76b'}
            ),
            'email': forms.EmailInput(
                attrs={'class': 'form-control',
                       'placeholder':'info@oscloud.com'}
            ),
            'tipo': forms.Select(
                attrs={'class': 'form-control'}
            ),
        }
