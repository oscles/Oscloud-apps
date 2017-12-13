from enum import Enum
from operator import sub, ne, mul, floordiv
from django.db import models

# Create your models here.
from ..mixins import TimeStampedModel
from ..clientes.models import Cliente
from ..empleados.models import Empleado


class TipoProyecto(TimeStampedModel):
    nombre = models.CharField(max_length=60, unique=True)

    class Meta:
        verbose_name = 'tipo de Proyecto'
        verbose_name_plural = 'Tipos de Proyectos'
        db_table = 'tipo_proyecto'

    def __str__(self):
        return self.nombre


class Tecnologia(TimeStampedModel):
    nombre = models.CharField(max_length=60, unique=True)

    class Meta:
        db_table = 'tecnologia'

    def __str__(self):
        return self.nombre


class Proyecto(TimeStampedModel):
    class ESTADOS(Enum):
        none = (None, 'Seleccione...')
        iniciado = ('iniciado', 'Iniciado')
        incompleto = ('incompleto', 'En proceso')
        cancelado = ('cancelado', 'Cancelado')
        terminado = ('terminado', 'Terminado')

        @classmethod
        def get_value(cls, member):
            return cls[member].value[0]


    nombre = models.CharField(max_length=60, unique=True, )
    fecha_inicio = models.DateField(verbose_name='fecha de inicio', )
    fecha_entrega = models.DateField(verbose_name='fecha de entrega', )
    estado = models.CharField(max_length=10, choices=[x.value for x in ESTADOS], )
    imagen_proyecto = models.ImageField(blank=True, null=True, upload_to='img-proyectos/', )
    valor_proyecto = models.PositiveIntegerField(verbose_name='valor del proyecto')
    progreso = models.SmallIntegerField(blank=True)
    cliente = models.ForeignKey(Cliente, blank=True, on_delete=models.CASCADE, )
    tipo = models.ManyToManyField(TipoProyecto, db_table='proyecto_has_tipo', )
    tecnologias = models.ManyToManyField(Tecnologia, db_table='proyecto_has_tecnologia', )
    empleados = models.ManyToManyField(Empleado, verbose_name='asignar empleados',
                                       db_table='proyecto_has_empleado', blank=True, )

    class Meta:
        db_table = 'proyecto'


    def __str__(self):
        return self.nombre


    def save(self, *args, **kwargs):
        self.progreso = self.__set_progreso()
        super(Proyecto, self).save(*args, **kwargs)


    def __set_progreso(self):
        dict_estado_proyectos = self.__diccionario_estados_progreso()
        estado = str(self.estado).lower()
        if estado not in dict_estado_proyectos:
            return dict_estado_proyectos.get('iniciado')
        return dict_estado_proyectos.get(estado)


    def __diccionario_estados_progreso(self):
        return {
            'terminado': 100,
            'incompleto': 75,
            'iniciado': 30,
            'cancelado': 0
        }


    def cant_horas_por_empleado(self):
        cant_dias = sub(self.fecha_entrega, self.fecha_inicio)
        cant_horas_diarias = floordiv(mul(cant_dias.days, 24), 8)
        cant_horas_empleado = floordiv(cant_horas_diarias, self.empleados.count())
        return cant_horas_empleado if ne(self.estado, 'cancelado') else 0
