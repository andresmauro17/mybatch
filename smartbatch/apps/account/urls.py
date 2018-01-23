from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [   
   
    path('login/', views.LoginClass.as_view(), name='login'),
    # url(r'^login/$', LoginClass.as_view(), name='login'),
    # url(r'^logout/', logout, name = 'logout'),
    # url(r'^register/$', RegisterClass, name='register'),
   
    
]
