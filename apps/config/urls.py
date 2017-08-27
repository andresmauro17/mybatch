
from django.conf.urls import url
from .views import EquipementCreateClass
from .views import EquipementListClass
from .views import EquipementUpdateClass
from .views import equipement_index


urlpatterns = [

	# url(r'^crear/$', EquipoCreate, name='equipo_create'),
	url(r'^equipment/index', equipement_index, name = "equipment_index"),
	url(r'^equipment/create', EquipementCreateClass.as_view(), name = "equipment_create"),
	url(r'^equipment/list', EquipementListClass.as_view(), name = "equipment_list"),
	url(r'^equipment/edit/(?P<pk>\d+)/$', EquipementUpdateClass.as_view(), name='equipement_edit'),
   
]
