# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import models

from django.contrib import admin

# Register your models here.

@admin.register(models.Empresa)
class EmpresaAdmin(admin.ModelAdmin):
    list_display = ['nombre','pais','nit', 'ciudad', 'direccion', 'telefono', 'sitioweb', 'mail', 'logo']
    list_editable = ['pais']
    ordering = ['nombre']

@admin.register(models.Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ['usuario','tipo_usuario','empresa']
    list_editable = ['tipo_usuario']
    ordering = ['usuario']
