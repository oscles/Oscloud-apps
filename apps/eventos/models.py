from django.db import models

# Create your models here.
from datetime import datetime

from ..mixins import TimeStampedModel


class Evento(TimeStampedModel):
    titulo = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=400, blank=True)
    fecha = models.DateField(blank=True)

    class Meta:
        db_table = 'evento'
