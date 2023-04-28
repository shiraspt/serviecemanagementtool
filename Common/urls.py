from django.urls import path
from . import views
app_name='Common'
urlpatterns = [
    path("home",views.home,name='home'),
    path("manager_login",views.manager_login),
    path("cce_login",views.cce_login),
    path("tec_login",views.tec_login)
]