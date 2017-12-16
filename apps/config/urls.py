
from django.conf.urls import url
from .views import EquipmentCreateClass
from .views import EquipmentListClass
from .views import EquipmentUpdateClass
from .views import EquipmentDetailClass
from .views import equipment_index
from .views import GeneratePdf
from .views import EquipmentDelete


from .views import MaterialCreateClass
from .views import MaterialListClass
from .views import MaterialUpdateClass
from .views import MaterialDetailClass
# from .views import Material_index
from .views import MaterialDelete
from .views import MaterialGeneratePdf
from .views import Material_index


urlpatterns = [

	# url(r'^crear/$', EquipoCreate, name='equipo_create'),
	url(r'^equipment/index', equipment_index, name = "equipment_index"),
	url(r'^equipment/create', EquipmentCreateClass.as_view(), name = "equipment_create"),
	url(r'^equipment/list', EquipmentListClass.as_view(), name = "equipment_list"),
	url(r'^equipment/edit/(?P<pk>\d+)/$', EquipmentUpdateClass.as_view(), name='equipment_edit'),
	url(r'^equipment/detail/(?P<pk>\d+)/$', EquipmentDetailClass.as_view(), name='equipment_detail'),
	url(r'^equipment/delete/(?P<pk>\d+)/$',EquipmentDelete.as_view(), name='equipment_delete'),
	url(r'^equipment/pdf_list/$', GeneratePdf.as_view(), name='equipment_pdf_list'),

	url(r'^material/index', Material_index, name = "material_index"),
    url(r'^material/list', MaterialListClass.as_view(), name = "material_list"),
     url(r'^material/edit//(?P<pk>\d+)/$', MaterialUpdateClass.as_view(), name = "material_edit"),
     url(r'^material/create', MaterialCreateClass.as_view(), name = "material_create"),
     url(r'^material/pdf_list/$', MaterialGeneratePdf.as_view(), name='material_pdf_list'),
        url(r'^material/detail/(?P<pk>\d+)/$', MaterialDetailClass.as_view(), name='material_detail'),
        url(r'^material/delete/(?P<pk>\d+)/$',MaterialDelete.as_view(), name='material_delete'),

]
