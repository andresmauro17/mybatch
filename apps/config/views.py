# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.views.generic import CreateView

from django.core.urlresolvers import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Equipo

from .forms import EquipoForm

# def EquipoCreate(request):
# 	return render(request, 'config/equipo_create.html', {})


class EquipoCreate(LoginRequiredMixin, CreateView):
	model = Equipo
	template_name = 'config/equipo_create.html'
	form_class = EquipoForm
	success_url = reverse_lazy('dashboard')