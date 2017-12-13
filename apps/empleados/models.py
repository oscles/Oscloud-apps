from django.contrib.auth.models import User
from django.db import models


# Create your models here.
from apps.mixins import TimeStampedModel


class CargoEmpleado(TimeStampedModel):
    nombre = models.CharField(max_length=60, unique=True)

    class Meta:
        verbose_name = 'cargo de empleado'
        verbose_name_plural = 'cargos de empleados'
        db_table = 'cargo_empleado'

    def __str__(self):
        return self.nombre


class Skill(TimeStampedModel):
    nombre = models.CharField(max_length=45, unique=True)

    class Meta:
        db_table = 'skill'

    def __str__(self):
        return self.nombre


class Empleado(TimeStampedModel, User):
    telefono = models.CharField(max_length=10)
    direccion = models.CharField(max_length=60)
    fecha_nacimiento = models.DateField(verbose_name='fecha de nacimiento')
    foto = models.ImageField(upload_to='img-empleados/', blank=True, )
    url = models.URLField(blank=True)
    profesion = models.CharField(max_length=45)
    perfil = models.TextField()
    cargo_empleado = models.ManyToManyField(CargoEmpleado,
                                            verbose_name='cargos', db_table='empleado_has_cargo', )
    skills = models.ManyToManyField(Skill, through='SkillEmpleado')

    class Meta:
        db_table = 'empleado'

    def __str__(self):
        return '{0} {1}'.format(self.first_name, self.last_name)


class SkillEmpleado(TimeStampedModel):
    id_skill = models.ForeignKey(Skill)
    id_empleado = models.ForeignKey(Empleado)
    anios_experiencia = models.SmallIntegerField(verbose_name='años de experiencia', )

    class Meta:
        db_table = 'empleado_has_skill'