from django.conf.urls import url

from .views import LoginClass
from .views import logout


urlpatterns = [    
    # url(r'^login/$', LoginClass, name='login'),
    url(r'^login/$', LoginClass.as_view(), name='login'),
    url(r'^logout/', logout, name = 'logout'),
   
    
]
