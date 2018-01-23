# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django

from django.shortcuts import redirect
from django.views.generic import View
from django.http import HttpResponse
from .forms import LoginUserForm



class LoginClass(View):
	form = LoginUserForm()
	message = None 
	template = 'account/login.html'

	def get(self, request, *args, **kwargs):
		if request.user.is_authenticated:			
			return redirect('home')
		return render(request, self.template, self.get_contexto())

	def post(self, request, *args, **kwargs):
		username_post = request.POST['username']
		password_post = request.POST['password']
		user = authenticate(username = username_post, password = password_post)

		if user is not None:
			login_django(request,user)
			return redirect('home')		
		else:
			self.message = "usuario o pasword incorrecto"
		return render(request, self.template, self.get_contexto())

	def get_contexto(self):
		return{'form':self.form, 'message':self.message}


	