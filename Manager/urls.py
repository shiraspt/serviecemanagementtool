from django.urls import path
from . import views
app_name='Manager'
urlpatterns = [
    path("manager_home",views.manager_home,name='manager_home'),
    
    path("add_cce",views.add_cce,name='add_cce'),
    path("add_tec",views.add_tec,name='add_tec'),
    path("add_models",views.add_models,name='add_models'),
    path("work_list",views.work_list,name='work_list'),
    path("view_work/<int:cid>",views.view_work,name='view_work'),
    path("view_report/<int:cid>",views.view_report,name='view_report'),
    path("view_tec",views.view_tec,name='view_tec'),
    path("tec_profile/<int:tid>",views.tec_profile,name='tec_profile'),
    path("update_tech/<int:tid>",views.update_tech,name='update_tech'),
    path("logout",views.logout,name='logout'),
    # path("search",views.search,name='search')

]