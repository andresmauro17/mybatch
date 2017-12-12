
from django.conf.urls import url
from .views import EquipmentCreateClass
from .views import EquipmentListClass
from .views import EquipmentUpdateClass
from .views import EquipmentDetailClass
from .views import equipment_index
from .views import GeneratePdf
from .views import EquipmentDelete
from .views import material_index


urlpatterns = [

	# url(r'^crear/$', EquipoCreate, name='equipo_create'),
	url(r'^equipment/index', equipment_index, name = "equipment_index"),
	url(r'^equipment/create', EquipmentCreateClass.as_view(), name = "equipment_create"),
	url(r'^equipment/list', EquipmentListClass.as_view(), name = "equipment_list"),
	url(r'^equipment/edit/(?P<pk>\d+)/$', EquipmentUpdateClass.as_view(), name='equipment_edit'),
	url(r'^equipment/detail/(?P<pk>\d+)/$', EquipmentDetailClass.as_view(), name='equipment_detail'),
	url(r'^equipment/delete/(?P<pk>\d+)/$',EquipmentDelete.as_view(), name='equipment_delete'),
	url(r'^equipment/pdf_list/$', GeneratePdf.as_view(), name='equipment_pdf_list'),
	url(r'^material/index', material_index, name = "material_index"),
   
]
