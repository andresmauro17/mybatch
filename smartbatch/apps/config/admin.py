# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import models

from django.contrib import admin

# Register your models here.

@admin.register(models.Equipo)
class EquipoAdmin(admin.ModelAdmin):
    # list_display = [ 'empresa','codigo','descripcion','fabricante','capacidad_maxima','capacidad_minima','unidad','fecha_calibracion','calibrable','calificado','estado','otras_caracteristicas','ficha_tecnica']
    list_display = [ 'empresa','codigo','descripcion','fabricante','capacidad_maxima','capacidad_minima','unidad','fecha_calibracion','calificado']
    list_editable = []
    ordering = ['codigo']
    autocomplete_fields = ['empresa',]


@admin.register(models.Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ['empresa','tipo','codigo','descripcion','unidad', 'pureza_maxima','pureza_minima','ficha_seguridad']
    list_editable = ['codigo','descripcion']
    ordering = ['codigo']
    autocomplete_fields = ['empresa','fabricante']



@admin.register(models.Proveedor)
class ProveedorAdmin(admin.ModelAdmin):
    list_display = ['empresa','nombre_proveedor']
    list_editable = ['nombre_proveedor']
    ordering = ['nombre_proveedor']
    autocomplete_fields = ['empresa']
    

	
@admin.register(models.Fabricante)
class FabricanteAdmin(admin.ModelAdmin):
    list_display = ['empresa', 'nombre_fabricante']
    list_editable = ['nombre_fabricante']
    ordering = ['nombre_fabricante']
    autocomplete_fields = ['empresa']
    search_fields = ['nombre_fabricante']