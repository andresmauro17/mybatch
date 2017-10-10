# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-11 21:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Equipo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=50, unique=True)),
                ('descripcion', models.CharField(max_length=50)),
                ('marca', models.CharField(default='No aplica', max_length=50)),
                ('capacidad_maxima_de_operacion', models.CharField(max_length=50)),
                ('unidad', models.CharField(choices=[('TON', 'Toneladas'), ('L', 'Litros'), ('KG', 'Kilogramos'), ('G', 'Gramos'), ('LB', 'Libras')], max_length=5)),
                ('ficha_tecnica', models.FileField(upload_to='pdf/config/equipo')),
                ('fecha_calibracion', models.DateField(blank=True, null=True)),
                ('estado', models.CharField(blank=True, choices=[('M', 'En mantenimiento'), ('A', 'Activo'), ('I', 'Inactivo')], max_length=1, null=True)),
                ('foto', models.FileField(blank=True, null=True, upload_to='img/config/equipo')),
            ],
        ),
    ]