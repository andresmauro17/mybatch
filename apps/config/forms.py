from django import forms

from .models import Equipo

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

		