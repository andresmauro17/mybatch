from django.conf.urls import url
from django.urls import path

from . import views

app_name="account"

urlpatterns = [   
   
    path('login/', views.LoginClass.as_view(), name='login'),
    path('logout/', views.logout, name = 'logout'),
    path('register/', views.register, name='register'),
   
    
]
