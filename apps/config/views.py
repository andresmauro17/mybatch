# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.views.generic import CreateView
from django.views.generic import ListView
from django.views.generic import UpdateView

from django.core.urlresolvers import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Equipo

from .forms import EquipoForm

def equipement_index(request):
	return render(request, 'config/equipement/equipement_index.html', {})


class EquipementCreateClass(LoginRequiredMixin, CreateView):
	login_url = 'account:login'
	model = Equipo
	template_name = 'config/equipement/equipement_create.html'
	form_class = EquipoForm
	success_url = reverse_lazy('dashboard')

class EquipementListClass(LoginRequiredMixin, ListView):
	login_url = 'account:login'
	model = Equipo 
	template_name = 'config/equipement/equipement_list.html'

class EquipementUpdateClass(LoginRequiredMixin, UpdateView):
	login_url = 'account:login'
	model = Equipo
	form_class = EquipoForm
	template_name = 'config/equipement/equipement_edit.html'
	success_url = reverse_lazy('dashboard')