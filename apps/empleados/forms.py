from django import forms

from apps.empleados.models import Skill, CargoEmpleado, Empleado


class FormSkill(forms.ModelForm):
    class Meta:
        model = Skill
        fields = ('nombre',)


class FormEmpleado(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = (
            'first_name',
            'last_name',
            'telefono',
            'direccion',
            'email',
            'fecha_nacimiento',
            'foto',
            'url',
            'profesion',
            'perfil',
            'cargo_empleado',
            'skills',
        )

        widgets = {
            'first_name': forms.TextInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Ej. Karl Tomas'
                       }
            ),
            'last_name': forms.TextInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Ej. Miranda C.'}
            ),
            'telefono': forms.TextInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Ej. 300 546 2345'}
            ),
            'direccion': forms.TextInput(
                attrs={'class': 'form-control',
                       'placeholder': ' Cartagena, Colombia, Co'}
            ),
            'email': forms.EmailInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Ej. info@oscloud.com'},
            ),
            'fecha_nacimiento': forms.DateInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Ej. 1980-08-23'}
            ),
            'foto': forms.FileInput(),
            'url': forms.TextInput(
                attrs={'class': 'form-control',
                       'placeholder': 'www.oscloud.co'}
            ),
            'profesion': forms.TextInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Ing de sistemas'}
            ),
            'perfil': forms.Textarea(
                attrs={'class': 'form-control',
                       'placeholder': 'Escriba un descripción acerca de'
                                      ' sus virtudes mínimo 20 palabras',
                       'rows': 4}
            ),
            'cargo_empleado': forms.SelectMultiple(
                attrs={'class': 'form-control js-example-basic-multiple'}
            ),
        }


class FormCargoEmpleado(forms.ModelForm):
    class Meta:
        model = CargoEmpleado
        fields = ('nombre',)
