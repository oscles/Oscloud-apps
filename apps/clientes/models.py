from enum import Enum

from django.db import models

# Create your models here.
from ..mixins import TimeStampedModel


class Cliente(TimeStampedModel):
    class TIPO_CLIENTE(Enum):
        none = (None, 'Seleccione..')
        natural = ('natural', 'Persona Natural')
        juridica = ('jurídica', 'Persona Jurídica')

    nombre = models.CharField(max_length=45)
    apellido = models.CharField(max_length=45)
    telefono = models.CharField(max_length=10)
    direccion = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    tipo = models.CharField(max_length=17, choices=[x.value for x in TIPO_CLIENTE])

    class Meta:
        db_table = 'cliente'

    def __str__(self):
        return '{0} {1}'.format(self.nombre, self.apellido)
