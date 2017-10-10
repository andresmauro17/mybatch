# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin

from .models import Cliente
from .models import Empresa

class ClienteAdmin(admin.ModelAdmin):
	exclude = ('usuario',)

class ClienteInline(admin.StackedInline):
	model = Cliente
	can_delete = False

class UserAdmin(AuthUserAdmin):
	inlines = [ClienteInline]

admin.site.unregister(User)#desregistro el user
admin.site.register(User, UserAdmin)
admin.site.register(Empresa)
# admin.site.register(Cliente, ClienteAdmin)