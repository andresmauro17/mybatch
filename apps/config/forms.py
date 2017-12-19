from django import forms

from .models import Equipo
from .models import Material

class EquipoForm(forms.ModelForm):

	class Meta:
		model = Equipo
		exclude = ["empresa"]

		fields = [
			'codigo',
			'descripcion',
			'marca',
			'capacidad_maxima_de_operacion',
			'unidad',
			'ficha_tecnica',
			'fecha_calibracion',
			'estado',
			'foto1',
			'foto2',
			'foto3',
		]

		labels = {
			'codigo':'Codigo del Equipo *',
			'descripcion':'Descripcion del Equipo *',
			'marca':'Marca *',
			'capacidad_maxima_de_operacion':'Capacidad Maxima de Operacion *',
			'unidad':'Unidad de Medida *',
			'ficha_tecnica':'Ficha Tecnica *',
			'fecha_calibracion':'Fecha de Calibracion',
			'estado':'Estado *',
			'foto1':'Foto1',
			'foto2':'Foto2',
			'foto3':'Foto3',
		}

		widgets = {
			'codigo':forms.TextInput(attrs={'class':'form-control','type':'text','required':'true'}),
			'descripcion':forms.TextInput(attrs={'class':'form-control','type':'text','required':'true'}),
			'marca':forms.TextInput(attrs={'class':'form-control','type':'text','required':'true'}),
			'capacidad_maxima_de_operacion':forms.NumberInput(attrs={'class':'form-control','required':'true'}),
			'unidad':forms.Select(attrs={'class':'selectpicker','data-style':'btn btn-info btn-sm btn-round', 'required':'true'}),
			'ficha_tecnica':forms.FileInput(attrs={}),
			'fecha_calibracion':forms.DateInput(attrs={'class':'form-control datepicker'}),
			'estado':forms.Select(attrs={'class':'selectpicker','data-style':'btn btn-info btn-sm btn-round', 'required':'true'}),
			'foto1':forms.FileInput(attrs={'class':''}),
			'foto2':forms.FileInput(attrs={'class':''}),
			'foto3':forms.FileInput(attrs={'class':''}),
		}

class MaterialForm(forms.ModelForm):
	class Meta:
		model = Material
		exclude = ["empresa"]

		fields = [
			'codigo',
			'descripcion',
			'proveedor',
			'fabricante',
			'unidad_UMB',
			'ficha_tecnica',
			'concentracion',
			'N_de_lote_fabricante',
			'fecha_de_vencimiento',
			'estado',
			'certificado_calidad',
			'costo_UMB',
		]

		labels = {
			'codigo' : 'Codigo del Material *',
			'descripcion' : 'Descripcion del Material *',
			'proveedor' : 'Proveedor del Material *',
			'fabricante' : 'Fabricante del Material *',
			'unidad_UMB' : 'Unidad de Medida Basica UMB *',
			'ficha_tecnica' : 'Ficha Tecnica del Material',
			'concentracion' : 'Concentracion del Material',
			'N_de_lote_fabricante' : 'Numero de Lote del Fabricante',
			'fecha_de_vencimiento' : 'Fecha de Vencimiento',
			'estado' : 'Estado',
			'certificado_calidad' : 'Certificado de Calidad',
			'costo_UMB' : 'Costo de la Unidad de Medida Basica *',
		}

		widgets = {
			'codigo':forms.TextInput(attrs={'class':'form-control','type':'text','required':'true'}),
			'descripcion':forms.TextInput(attrs={'class':'form-control','type':'text','required':'true'}),
			# 'proveedor'
			# 'fabricante',
			'unidad_UMB':forms.Select(attrs={'class':'selectpicker','data-style':'btn btn-info btn-sm btn-round', 'required':'true'}),
			'ficha_tecnica':forms.FileInput(attrs={}),
			'concentracion':forms.TextInput(attrs={'class':'form-control','type':'text','required':'true'}),
			'N_de_lote_fabricante':forms.TextInput(attrs={'class':'form-control','type':'text','required':'true'}),
			'fecha_de_vencimiento':forms.DateInput(attrs={'class':'form-control datepicker'}),
			'estado':forms.Select(attrs={'class':'selectpicker','data-style':'btn btn-info btn-sm btn-round', 'required':'true'}),
			'certificado_calidad':forms.FileInput(attrs={}),
			'costo_UMB':forms.TextInput(attrs={'class':'form-control','type':'text','required':'true'}),
		}