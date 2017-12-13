from django import forms

from .models import Proyecto, TipoProyecto, Tecnologia


class FormProyectos(forms.ModelForm):
    class Meta:
        model = Proyecto
        fields = (
            'nombre',
            'fecha_inicio',
            'fecha_entrega',
            'estado',
            'imagen_proyecto',
            'valor_proyecto',
            'cliente',
            'tipo',
            'tecnologias',
            'empleados',
        )

        widgets = {
            'nombre': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Ej. Web Oscloud Tecnología'}),
            'fecha_inicio': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'type': 'text',
                    'placeholder': 'Ejemplo 2017-02-03'
                }
            ),
            'fecha_entrega': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'type': 'text',
                    'placeholder': 'Ejemplo 2017-02-03'
                }
            ),
            'estado': forms.Select(attrs={'class': 'form-control'}),
            'imagen_proyecto': forms.FileInput(
                attrs={
                    'class': 'form-control-file',
                    'id': 'exampleFormControlFile1',
                    'type': 'file'
                }
            ),
            'valor_proyecto': forms.NumberInput(attrs={'class': 'form-control'}),
            'cliente': forms.Select(attrs={'class': 'form-control js-example-basic-single'}),

            'tipo': forms.SelectMultiple(
                attrs={'class': 'form-control js-example-basic-multiple'}),

            'tecnologias': forms.SelectMultiple(
                attrs={'class': 'form-control js-example-basic-multiple', }),

            'empleados': forms.SelectMultiple(
                attrs={'class': 'form-control js-example-basic-multiple'}),
        }

    def clean_fecha_entrega(self):
        fecha_inicio = self.cleaned_data.get('fecha_inicio')
        fecha_entrega = self.cleaned_data.get('fecha_entrega')
        if fecha_entrega < fecha_inicio:
            raise forms.ValidationError \
                ('La fecha de inicio no debe ser superior a la de entrega')
        return fecha_entrega


class FormTipoProyecto(forms.ModelForm):
    class Meta:
        model = TipoProyecto
        fields = ('nombre',)


class FormTecnologia(forms.ModelForm):
    class Meta:
        model = Tecnologia
        fields = ('nombre',)
