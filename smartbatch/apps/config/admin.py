# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import models

from django.contrib import admin

# Register your models here.

@admin.register(models.Equipo)
class EmpresaAdmin(admin.ModelAdmin):
    # list_display = [ 'empresa','codigo','descripcion','fabricante','capacidad_maxima','capacidad_minima','unidad','fecha_calibracion','calibrable','calificado','estado','otras_caracteristicas','ficha_tecnica']
    list_display = [ 'empresa','codigo','descripcion','fabricante','fecha_calibracion','calificado','estado','otras_caracteristicas','ficha_tecnica']
    list_editable = ['codigo','descripcion']
    ordering = ['codigo']
    autocomplete_fields = ['empresa']


   