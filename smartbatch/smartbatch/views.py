from django.shortcuts import render

from django.shortcuts import redirect

from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required



def home(request):
	# if request.user.is_authenticated():
	# 	return redirect('dashboard')

	return render(request, 'pricing.html', {})

def error_404(request):
	return render(request, 'error_404.html', {})	

@login_required(login_url = 'account:login')
def dashboard(request):
	return render(request, 'dashboard.html')


