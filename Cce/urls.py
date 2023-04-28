from django.urls import path
from . import views
app_name='Cce'

urlpatterns = [
    path("cce_home",views.cce_home,name='cce_home'),
    path("register_work",views.register_work,name='register_work'),
    path("model_select",views.model_select,name='model_select'),
    path("tec_select",views.tec_select,name='tec_select'),
    path("added_data/<int:cid>",views.added_data,name='added_data'),
    path("update_complaint/<int:cid>",views.update_complaint,name='update_complaint'),
    path("view_complaint/<int:cid>",views.view_complaint,name='view_complaint'),
    path("complaint_list",views.complaint_list,name='complaint_list'),
    path('logout',views.logout,name='logout')


]



