# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

from django.contrib.auth.models import User

class Empresa(models.Model):
	nombre = models.CharField(max_length=100)
	pais_CHOICES = (
	    ('Colombia', 'Colombia'),
	    ('Mexico','Mexico'),	      
	)
	pais = models.CharField(		
		max_length=20,
		choices=pais_CHOICES,
		) 
	nit = models.CharField(max_length=100, blank=True, null=True)
	ciudad = models.CharField(max_length=50, blank=True, null=True)
	direccion = models.CharField(max_length=50, blank=True, null=True)
	telefono = models.CharField(max_length=50, blank=True, null=True)
	sitioweb = models.URLField(blank=True, null=True)
	mail = models.EmailField(blank=True, null=True)
	logo = models.ImageField(upload_to='img/account/empresa', blank=True, null=True)# tamanio de 178 px de ancho por 51 alto

	def __str__(self):
			return self.nombre

class Cliente(models.Model):
	usuario = models.OneToOneField(User, on_delete =  models.CASCADE)
	tipo_usuario_CHOICES = (
	    ('Administrador', 'administrador'),
	    ('Limitado','Limitado'),	      
	)
	tipo_usuario = models.CharField(		
		max_length=20,
		choices=tipo_usuario_CHOICES,
		)
	empresa = models.ForeignKey(Empresa, on_delete = models.CASCADE)

	def __str__(self):
		return self.usuario.username