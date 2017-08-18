# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Equipo(models.Model):
	codigo = models.CharField(max_length=50, unique=True)
	descripcion = models.CharField(max_length=150)
	marca = models.CharField(max_length=50, default='no aplica')
	capacidad_maxima_de_operacion= models.IntegerField()
	UNIDAD_CHOICES = (
	    ('TON', 'Toneladas'),
	    ('L','Litros'),
	    ('KG','Kilogramos'),
	    ('G','Gramos'),
	    ('LB','Libras'),    
	)
	unidad = models.CharField(
	    max_length=5,
	    choices=UNIDAD_CHOICES,	    
	)
	
	ficha_tecnica = models.FileField(upload_to='pdf/config/equipo')
	fecha_calibracion = models.DateField(blank=True, null=True)
	ESTADO_CHOICES = (
	    ('M', 'En mantenimiento'),
	    ('A','Activo'),
	    ('I','Inactivo'),	    
	)
	estado = models.CharField(
	    max_length=1,
	    choices=ESTADO_CHOICES,
	    blank=True,
	    null=True
	)
	foto1 = models.FileField(upload_to='img/config/equipo', blank=True, null=True)
	foto2 = models.FileField(upload_to='img/config/equipo', blank=True, null=True)
	foto3 = models.FileField(upload_to='img/config/equipo', blank=True, null=True)


	def __str__(self):
		return self.codigo


