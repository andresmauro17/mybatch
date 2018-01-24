
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import absolute_import

from django.db import models

# Create your models here.

from apps.account.models import Empresa

class Equipo(models.Model):
    empresa = models.ForeignKey(Empresa, on_delete = models.CASCADE)
    codigo = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=150)
    fabricante = models.CharField(max_length=50,)
    capacidad_maxima= models.DecimalField(max_digits=5, decimal_places=2)
    capacidad_minima= models.DecimalField(max_digits=5, decimal_places=2)
    UNIDAD_CHOICES = (
        ('TON', 'Toneladas'),
        ('L','Litros'),
        ('KG','Kilogramos'),
        ('G','Gramos'),
        ('LB','Libras'),
    )
    unidad = models.CharField(
    max_length=20,
    choices=UNIDAD_CHOICES,
    )
    fecha_calibracion = models.DateField(blank=True, null=True)
    calibrable = models.BooleanField()

    CALIFICADO_CHOICES = (
        ('SI', 'SI'),
        ('NO','NO'),
        ('NA','NO APLICA'),
    )
    calificado = models.CharField(
    max_length=15,
    choices=CALIFICADO_CHOICES,	
    )

    ESTADO_CHOICES = (
        ('MANTENIMIENTO', 'En mantenimiento'),
        ('ACTIVO','Activo'),
        ('INACTIVO','Inactivo'),
    )
    estado = models.CharField(
    max_length=20,
    choices=ESTADO_CHOICES,

    )
    otras_caracteristicas = models.TextField(blank=True, null=True)
    ficha_tecnica = models.FileField(upload_to='pdf/config/equipo', blank=True, null = True,)


    def __str__(self):
        return self.codigo