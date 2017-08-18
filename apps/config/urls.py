
from django.conf.urls import url
from .views import EquipoCreate



urlpatterns = [

	# url(r'^crear/$', EquipoCreate, name='equipo_create'),
	url(r'^equipment/create', EquipoCreate.as_view(), name = "equipment_create"),
   
]
