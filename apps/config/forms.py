from django import forms

from .models import Equipo

class EquipoForm(forms.ModelForm):

	class Meta:
		model = Equipo

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
			'codigo':'Codigo del equipo', 
			'descripcion':'Descripcion del equipo', 
			'marca':'Marca', 
			'capacidad_maxima_de_operacion':'Capacidad maxima de operacion', 
			'unidad':'unidad',			
			'ficha_tecnica':'ficha_tecnica', 
			'fecha_calibracion':'Fecha de calibracion', 
			'estado':'estado', 
			'foto1':'foto1', 
			'foto2':'foto2', 
			'foto3':'foto3', 
		}

		widgets = {
			'codigo':forms.TextInput(attrs={'class':'form-control','type':'text','required':'true'}),
			'descripcion':forms.TextInput(attrs={'class':'form-control','type':'text','required':'true'}),
			'marca':forms.TextInput(attrs={'class':'form-control','type':'text','required':'true'}),
			'capacidad_maxima_de_operacion':forms.NumberInput(attrs={'class':'form-control','required':'true'}),			
			'unidad':forms.Select(attrs={'class':'selectpicker','data-style':'btn btn-info btn-sm btn-round'}),
			'ficha_tecnica':forms.FileInput(attrs={'class':''}),
			'fecha_calibracion':forms.DateInput(attrs={'class':'form-control datepicker'}),
			'estado':forms.Select(attrs={'class':'selectpicker','data-style':'btn btn-primary btn-round'}),
			'foto1':forms.FileInput(attrs={'class':''}),
			'foto2':forms.FileInput(attrs={'class':''}),
			'foto3':forms.FileInput(attrs={'class':''}),				
		}

		