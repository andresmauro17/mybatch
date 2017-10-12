# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import absolute_import

from django.db import models

from django.contrib.auth.models import User

class Empresa(models.Model):
	nombre = models.CharField(max_length=100)
	nit = models.CharField(max_length=100, blank=True, null=True)
	direccion = models.CharField(max_length=50, blank=True, null=True)
	ciudad = models.CharField(max_length=50, blank=True, null=True)
	telefono = models.CharField(max_length=50, blank=True, null=True)
	sitioweb = models.URLField(blank=True, null=True)
	mail = models.EmailField(blank=True, null=True)
	logo = models.ImageField(blank=True, null=True)# tamanio de 178 px de ancho por 51 alto

	def __str__(self):
			return self.nombre

class Cliente(models.Model):
	usuario = models.OneToOneField(User, on_delete =  models.CASCADE)
	tipo_usuario_CHOICES = (
	    ('A', 'administrador'),
	    ('L','Limitado'),	      
	)
	tipo_usuario = models.CharField(		
		max_length=20,
		choices=tipo_usuario_CHOICES,
		)
	empresa = models.ForeignKey(Empresa, on_delete = models.CASCADE)

	def __str__(self):
		return self.usuario.username

#     operations = [
# migrations.CreateModel(
#     name='Empresa',
#     fields=[
#         ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
#         ('nombre', models.CharField(blank=True, max_length=50, null=True)),
#         ('nit', models.CharField(blank=True, max_length=50, null=True)),
#         ('direccion', models.CharField(blank=True, max_length=50, null=True)),
#         ('telefono', models.CharField(blank=True, max_length=50, null=True)),
#         ('sitioweb', models.URLField(blank=True, null=True)),
#         ('mail', models.CharField(blank=True, max_length=50, null=True)),
#         ('logo', models.ImageField(blank=True, null=True, upload_to=b'')),
#     ],
# ),
# migrations.CreateModel(
#     name='PerfilUsuario',
#     fields=[
#         ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
#         ('tipo_usuario', models.CharField(choices=[('A', 'Administrador'), ('L', 'limtado')], max_length=20)),
#         ('empresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.Empresa')),
#         ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
#     ],
# ),
# ]