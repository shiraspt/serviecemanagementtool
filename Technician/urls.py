from django.urls import path
from . import views
app_name='Technician'

urlpatterns = [
    path("tec_home",views.tec_home,name='tec_home'),
    path("finished_work",views.finished_work,name='finished_work'),
    path("add_report/<int:cid>",views.add_report,name='add_report'),
    path("view_work/<int:cid>",views.view_work,name='view_work'),
    path("view_my_report/<int:cid>",views.view_my_report,name='view_my_report'),
    path("logout",views.logout,name='logout')
]
