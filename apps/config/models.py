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

class Proveedor(models.Model):
	nombre_proveedor = models.CharField(max_length=150)

	def __str__(self):
		return self.nombre_proveedor

class Fabricante(models.Model):
	nombre_fabricante = models.CharField(max_length=150)

	def __str__(self):
		return self.nombre_fabricante


class Material(models.Model):
	codigo = models.CharField(max_length=50, unique=True)
	descripcion = models.CharField(max_length=150)
	proveedor = models.ManyToManyField(Proveedor)
	fabricante = models.ManyToManyField(Fabricante)
	UNIDAD_CHOICES = (
	    ('TON', 'Toneladas'),
	    ('L','Litros'),
	    ('KG','Kilogramos'),
	    ('G','Gramos'),
	    ('LB','Libras'),    
	)
	unidad_UMB = models.CharField(
	    max_length=5,
	    choices=UNIDAD_CHOICES,	    
	)
	ficha_tecnica = models.FileField(upload_to='pdf/config/material/ficha_tecnica')
	concentracion = models.CharField(max_length=50, blank=True, null=True) 
	N_de_lote_fabricante = models.CharField(max_length=50, blank=True, null=True) 
	fecha_de_vencimiento = models.DateField(blank=True, null=True)
	ESTADO_CHOICES = (
	    ('aprobado', 'Aprobado'),
	    ('cuarentena','Cuarentena'),
	    ('rechazado','Rechazado'),	    
	)
	estado = models.CharField(
	    max_length=30,
	    choices=ESTADO_CHOICES,
	    blank=True,
	    null=True
	)	
	ficha_tecnica = models.FileField(upload_to='pdf/config/material/certificado_calidad')
	costo_UMB = models.CharField(max_length=150)

	def __str__(self):
		return self.codigo

class Producto(models.Model):
	producto = models.CharField(max_length=50)
	presentacion = models.CharField(max_length=50)
	materia_prima = models.ManyToManyField(Material)
	apariencia = models.CharField(max_length=100)
	ph = models.CharField(max_length=50)
	olor = models.CharField(max_length=50)
	color = models.CharField(max_length=50)
	volumen = models.CharField(max_length=50)
	grado_alcoholico = models.CharField(max_length=50)
	mesofilos_aerobios_totales = models.CharField(max_length=50)
	pseudomonas_aeruginosa = models.CharField(max_length=50)
	coliformes_totales = models.CharField(max_length=50)
	Staphylococus_aureus = models.CharField(max_length=50)

	def __str__(self):
		return self.producto