# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import absolute_import

from django.shortcuts import render

from django.views.generic import CreateView
from django.views.generic import ListView
from django.views.generic import UpdateView
from django.views.generic import DetailView
from django.views.generic import DeleteView
from django.views.generic import View

from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect
from django.http import HttpResponse


from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin

from .models import Equipo
from .models import Material

from apps.account.models import Empresa

from mybatch.utils import render_to_pdf

from .forms import EquipoForm
from django.utils import timezone


def equipment_index(request):
    return render(request, 'config/equipment/equipment_index.html', {})


class EquipmentCreateClass(LoginRequiredMixin, CreateView):
	login_url = 'account:login'
	model = Equipo
	template_name = 'config/equipment/equipment_create.html'
	form_class = EquipoForm
	success_url = reverse_lazy('config:equipment_list')
	success_message = 'equipo registrado de forma exitosa'

	def form_valid(self, form):
		self.object = form.save(commit=False)
		self.object.empresa = Empresa.objects.get(id=self.request.user.cliente.empresa.id)  # use your own profile here
		self.object.save()
		messages.success(self.request,self.success_message)
		return HttpResponseRedirect( self.get_success_url() )

class EquipmentListClass(LoginRequiredMixin, ListView):
	login_url = 'account:login'
	model = Equipo
	template_name = 'config/equipment/equipment_list.html'

	def get_queryset(self):
		return Equipo.objects.filter(empresa=self.request.user.cliente.empresa.id)



class EquipmentUpdateClass(LoginRequiredMixin, UpdateView):
	login_url = 'account:login'
	model = Equipo
	form_class = EquipoForm
	template_name = 'config/equipment/equipment_edit.html'
	success_url = reverse_lazy('config:equipment_list')
	success_message = 'equipo actualizado de forma exitosa'

	def form_valid(self, form):
		self.object = form.save(commit=False)
		self.object.empresa = Empresa.objects.get(id=self.request.user.cliente.empresa.id)  # use your own profile here
		self.object.save()
		messages.success(self.request,self.success_message)
		return HttpResponseRedirect( self.get_success_url() )

class EquipmentDetailClass(LoginRequiredMixin, DetailView):
	login_url = 'account:login'
	model = Equipo
	template_name = 'config/equipment/equipment_detail.html'


class EquipmentDelete(LoginRequiredMixin,DeleteView):
	login_url = 'account:login'
	model = Equipo
	template_name = 'config/equipment/equipment_delete.html'
	success_url = reverse_lazy('config:equipment_list')



class GeneratePdf(LoginRequiredMixin, ListView):
     login_url = 'account:login'
     model = Equipo
     def get(self, request, *args, **kwargs):
         data = {
             'amount': 39.99,
             'customer_name': 'Cooper Mann',
             'order_id': 1233434,
             'user':self.request.user,
             'date_time':timezone.now(),
             'object_list':Equipo.objects.filter(empresa=self.request.user.cliente.empresa.id),
         }
         pdf = render_to_pdf('config/equipment/equipment_list_pdf.html', data)
         return HttpResponse(pdf, content_type='application/pdf')


# +++++++++++++++++++ material +++++++++++++++++++++++++++++++++++++++++++++


def Material_index(request):
	return render(request, 'config/material/material_index.html', {})

class MaterialCreateClass(LoginRequiredMixin, CreateView):
    pass
# class MaterialCreateClass(LoginRequiredMixin, CreateView):
#     login_url = 'account:login'
#     model = Equipo
#     template_name = 'config/material/material_create.html'
#     form_class = EquipoForm
#     success_url = reverse_lazy('config:material_list')
#     success_message = 'equipo registrado de forma exitosa'

#     def form_valid(self, form):
#         self.object = form.save(commit=False)
#         self.object.empresa = Empresa.objects.get(id=self.request.user.cliente.empresa.id)  # use your own profile here
#         self.object.save()
#         messages.success(self.request,self.success_message)
#         return HttpResponseRedirect( self.get_success_url() )

class MaterialListClass(LoginRequiredMixin, ListView):
    login_url = 'account:login'
    model = Material
    template_name = 'config/material/material_list.html'

    def get_queryset(self):
        return Material.objects.filter(empresa=self.request.user.cliente.empresa.id)

class MaterialUpdateClass(LoginRequiredMixin, UpdateView):
    pass

# class MaterialUpdateClass(LoginRequiredMixin, UpdateView):
#     login_url = 'account:login'
#     model = Equipo
#     form_class = EquipoForm
#     template_name = 'config/material/material_edit.html'
#     success_url = reverse_lazy('config:material_list')
#     success_message = 'equipo actualizado de forma exitosa'

#     def form_valid(self, form):
#         self.object = form.save(commit=False)
#         self.object.empresa = Empresa.objects.get(id=self.request.user.cliente.empresa.id)  # use your own profile here
#         self.object.save()
#         messages.success(self.request,self.success_message)
#         return HttpResponseRedirect( self.get_success_url() )


class MaterialDetailClass(LoginRequiredMixin, DetailView):
    login_url = 'account:login'
    model = Material
    template_name = 'config/material/material_detail.html'

class MaterialDelete(LoginRequiredMixin,DeleteView):
    pass
# class MaterialDelete(LoginRequiredMixin,DeleteView):
#     login_url = 'account:login'
#     model = Equipo
#     template_name = 'config/material/material_delete.html'
#     success_url = reverse_lazy('config:material_list')

class MaterialGeneratePdf(LoginRequiredMixin, ListView):
    pass
# class MaterialGeneratePdf(LoginRequiredMixin, ListView):
#      login_url = 'account:login'
#      model = Equipo
#      def get(self, request, *args, **kwargs):
#          data = {
#              'amount': 39.99,
#              'customer_name': 'Cooper Mann',
#              'order_id': 1233434,
#              'user':self.request.user,
#              'date_time':timezone.now(),
#              'object_list':Equipo.objects.filter(empresa=self.request.user.cliente.empresa.id),
#          }
#          pdf = render_to_pdf('config/material/equipment_list_pdf.html', data)
#          return HttpResponse(pdf, content_type='application/pdf')

