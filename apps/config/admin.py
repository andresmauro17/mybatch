# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Equipo
from .models import Material
from .models import Fabricante
from .models import Proveedor
from .models import Producto

# Register your models here.

admin.site.register(Equipo)
admin.site.register(Material)
admin.site.register(Fabricante)
admin.site.register(Proveedor)
admin.site.register(Producto)

