from django.shortcuts import render,redirect
from Common.decorators import auth_manager

from Common.models import Manager
from Manager.models import Cce, Technician
from django.views.decorators.cache import cache_control
# Create your views here.
@cache_control(no_cache=True, must_revalidate=True,no_store=True)

# @auth_manager
def home(request):
    
    
    
    return render (request,"home.html")


@cache_control(no_cache=True, must_revalidate=True,no_store=True)

def manager_login(request):
    msg=""
    if request.method == 'POST':
         
         try:
             man_email=request.POST["manager_username"]
             man_pass=request.POST["manager_password"]
             manager  = Manager.objects.get(manager_email=man_email,manager_password=man_pass)
             request.session['manager']=manager.id
             return redirect('Manager:manager_home')
         
         except Exception as e:
             msg="Invalid username or password"
             print(e)

    return render (request,"manager_login.html",{'msg':msg})



@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def cce_login(request):
    msg=""
    if request.method == 'POST':
         
         try:
             cce_email=request.POST["cce_username"]
             cce_pass=request.POST["cce_password"]
             cce  = Cce.objects.get(cce_email=cce_email,cce_password=cce_pass)
             request.session['cce']=cce.id
             return redirect('Cce:cce_home')
         
         except Exception as e:
             msg="Invalid username or password"
             print(e)
    
    return render (request,"cce_login.html",{'msg':msg})
    
@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def tec_login(request):
    msg=""
    if request.method == 'POST':
         
         try:
             tec_usename=request.POST["tec_username"]
             tec_pass=request.POST["tec_password"]
             tec  = Technician.objects.get(tec_email=tec_usename,tec_password=tec_pass)
             request.session['technician']=tec.id
             return redirect('Technician:tec_home')
         
         except Exception as e:
             msg="Invalid username or password"
             print(e)
    
    
    return render (request,"tec_login.html",{'msg':msg})