# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import absolute_import

from django.shortcuts import render

from django.views.generic import CreateView
from django.views.generic import ListView
from django.views.generic import UpdateView

from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin

from .models import Equipo

from apps.account.models import Empresa

from .forms import EquipoForm

def equipement_index(request):
	return render(request, 'config/equipement/equipement_index.html', {})


class EquipementCreateClass(LoginRequiredMixin, CreateView):
	login_url = 'account:login'
	model = Equipo
	template_name = 'config/equipement/equipement_create.html'
	form_class = EquipoForm
	success_url = reverse_lazy('config:equipment_list')
	success_message = 'equipo registrado de forma exitosa'

	def form_valid(self, form):		
		self.object = form.save(commit=False)
		self.object.empresa = Empresa.objects.get(id=self.request.user.cliente.empresa.id)  # use your own profile here
		self.object.save()
		messages.success(self.request,self.success_message)
		return HttpResponseRedirect( self.get_success_url() )

class EquipementListClass(LoginRequiredMixin, ListView):
	login_url = 'account:login'
	model = Equipo 
	template_name = 'config/equipement/equipement_list.html'
	
	def get_queryset(self):		
		return Equipo.objects.filter(empresa=self.request.user.cliente.empresa.id)



class EquipementUpdateClass(LoginRequiredMixin, UpdateView):
	login_url = 'account:login'
	model = Equipo
	form_class = EquipoForm
	template_name = 'config/equipement/equipement_edit.html'
	success_url = reverse_lazy('config:equipment_list')
	success_message = 'equipo registrado de forma exitosa'

	def form_valid(self, form):		
		self.object = form.save(commit=False)
		self.object.empresa = Empresa.objects.get(id=self.request.user.cliente.empresa.id)  # use your own profile here
		self.object.save()
		messages.success(self.request,self.success_message)
		return HttpResponseRedirect( self.get_success_url() )