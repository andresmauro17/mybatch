# -*- coding: utf-8 -*-

from django import forms
from django.contrib.auth.models import User


class LoginUserForm(forms.Form):
	username = forms.CharField(max_length=20, label = 'Usuario')
	password = forms.CharField(max_length= 20,label = 'Contraseña', widget=forms.PasswordInput())

	def __init__(self, *args, **kwargs):#utilizo el constructr de la clase form
		super(LoginUserForm, self).__init__(*args, **kwargs)#le digo que no sobreescriba el constructor sino que haga lo que ya hacia
		self.fields['username'].widget.attrs.update( {'id' : 'username_login' , 'class':'form-control'} )
		self.fields['password'].widget.attrs.update( {'id' : 'password_login' , 'class':'form-control'} )