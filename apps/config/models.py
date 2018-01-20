# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import absolute_import

from django.db import models
from apps.account.models import Empresa

# Create your models here.

class Equipo(models.Model):
	empresa = models.ForeignKey(Empresa, on_delete = models.CASCADE, default=1)##---- modificar el default -------
	codigo = models.CharField(max_length=50)
	descripcion = models.CharField(max_length=150)
	fabricante = models.CharField(max_length=50, default='no aplica')
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

	ficha_tecnica = models.FileField(upload_to='pdf/config/equipo', blank=True)
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
	empresa = models.ForeignKey(Empresa, on_delete = models.CASCADE, default=1)##---- modificar el default -------
	# codigo
	nombre_proveedor = models.CharField(max_length=150)

	def __str__(self):
		return self.nombre_proveedor

class Fabricante(models.Model):
	empresa = models.ForeignKey(Empresa, on_delete = models.CASCADE, default=1)##---- modificar el default -------
	# codigo
	nombre_fabricante = models.CharField(max_length=150)

	def __str__(self):
		return self.nombre_fabricante


class Material(models.Model):
	empresa = models.ForeignKey(Empresa, on_delete = models.CASCADE, default=1)##---- modificar el default -------
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
	ficha_tecnica = models.FileField(upload_to='pdf/config/material/ficha_tecnica', blank=True)
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
	certificado_calidad = models.FileField(upload_to='pdf/config/material/certificado_calidad', blank=True, null=True)
	costo_UMB = models.CharField(max_length=150)

	def __str__(self):
		return self.codigo


# codigo
# descripcion
# proveedor
# fabricante
# unidad_UMB
# ficha_tecnica
# concentracion
# N_de_lote_fabricante
# fecha_de_vencimiento
# estado
# certificado_calidad
# costo_UMB


class Producto(models.Model):
	empresa = models.ForeignKey(Empresa, on_delete = models.CASCADE, default=1)##---- modificar el default -------
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
