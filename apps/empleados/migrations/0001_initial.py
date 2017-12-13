# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-12-08 00:16
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CargoEmpleado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('nombre', models.CharField(max_length=60, unique=True)),
            ],
            options={
                'verbose_name': 'cargo de empleado',
                'verbose_name_plural': 'cargos de empleados',
                'db_table': 'cargo_empleado',
            },
        ),
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('telefono', models.CharField(max_length=10)),
                ('direccion', models.CharField(max_length=60)),
                ('fecha_nacimiento', models.DateField(verbose_name='fecha de nacimiento')),
                ('foto', models.ImageField(blank=True, upload_to='img-empleados/')),
                ('url', models.URLField(blank=True)),
                ('profesion', models.CharField(max_length=45)),
                ('perfil', models.TextField()),
                ('cargo_empleado', models.ManyToManyField(db_table='empleado_has_cargo', to='empleados.CargoEmpleado', verbose_name='cargos')),
            ],
            options={
                'db_table': 'empleado',
            },
            bases=('auth.user', models.Model),
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('nombre', models.CharField(max_length=45, unique=True)),
            ],
            options={
                'db_table': 'skill',
            },
        ),
        migrations.CreateModel(
            name='SkillEmpleado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('anios_experiencia', models.SmallIntegerField(verbose_name='años de experiencia')),
                ('id_empleado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='empleados.Empleado')),
                ('id_skill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='empleados.Skill')),
            ],
            options={
                'db_table': 'empleado_has_skill',
            },
        ),
        migrations.AddField(
            model_name='empleado',
            name='skills',
            field=models.ManyToManyField(through='empleados.SkillEmpleado', to='empleados.Skill'),
        ),
    ]
