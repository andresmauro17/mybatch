# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.shortcuts import redirect

from django.views.generic import View

from .forms import LoginUserForm

from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django
from django.contrib.auth import logout as logout_django
from django.contrib.auth.decorators import login_required

# def LoginClass(request):
# 	return render(request, 'account/login.html')

def RegisterClass(request):
	return render(request, 'account/register.html')


class LoginClass(View):
	form = LoginUserForm()
	message = None 
	template = 'account/login.html'

	def get(self, request, *args, **kwargs):
		if request.user.is_authenticated():			
			return redirect('dashboard')
		return render(request, self.template, self.get_contexto())

	def post(self, request, *args, **kwargs):
		username_post = request.POST['username']
		password_post = request.POST['password']
		user = authenticate(username = username_post, password = password_post)

		if user is not None:
			login_django(request,user)
			return redirect('dashboard')		
		else:
			self.message = "usuario o pasword incorrecto"
		return render(request, self.template, self.get_contexto())

	def get_contexto(self):
		return{'form':self.form, 'message':self.message}

@login_required(login_url = 'account:login')
def logout(request):
	logout_django(request)
	return redirect('home')