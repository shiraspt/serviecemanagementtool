from datetime import date
from datetime import time
import datetime

from django.shortcuts import render,redirect
from django.core.mail import send_mail

from Cce.models import Complaint
from Common.decorators import auth_technician
from Manager.models import Technician
from Technician.models import Work_report
from smt import settings
from django.core.paginator import Paginator
from django.views.decorators.cache import cache_control


# Create your views here.
@cache_control(no_cache=True, must_revalidate=True,no_store=True)
@auth_technician
def tec_home(request):
    name=Technician.objects.get(id=request.session['technician']).tec_name
    my_works= Complaint.objects.filter(technician_id=request.session['technician']).exclude (work_status = 'Finished').order_by('-complaint_date','-complaint_name').values('id','customer_name','customer_phone1','technician_name','work_status','complaint_name')
    p = Paginator(my_works, 20)
    page_number = request.GET.get('page')
    # print(page_number)
    try:
        page_obj = p.get_page(page_number)
    except Exception as e:
        page_obj = p.page(1) 

    context = {
        'name':name,
        'page_obj':page_obj,
        'my_works':my_works
    }
    
    
    
    return render (request,"tec_home.html",context)
@cache_control(no_cache=True, must_revalidate=True,no_store=True)
@auth_technician
def finished_work(request):
    
    name=Technician.objects.get(id=request.session['technician']).tec_name
    my_works= Complaint.objects.filter(technician_id=request.session['technician'],work_status = 'Finished').order_by('-complaint_date','-complaint_name').values('id','customer_name','customer_phone1','technician_name','work_status','complaint_name')

    p = Paginator(my_works, 20)
    page_number = request.GET.get('page')
    # print(page_number)
    try:
        page_obj = p.get_page(page_number)
    except Exception as e:
        page_obj = p.page(1)
         

    context = {
        'name':name,
        'page_obj':page_obj,
        'my_works':my_works
    }
    
    return render (request,"finished_work.html",context)
@cache_control(no_cache=True, must_revalidate=True,no_store=True)
@auth_technician
def add_report(request,cid):
    name=Technician.objects.get(id=request.session['technician']).tec_name

    msg = ""
    complaint_data= Complaint.objects.get(id=cid)
    context = {
        'name':name,
        'msg':msg,
        'complaint_data':complaint_data
    }
    if request.method =='POST':
        try:
            today = date.today()
            time = datetime.datetime.now()
            report = request.POST['workreport']
           
            serial = request.POST['serialnumber']
            status = request.POST['work_status']
            warrenty = request.POST['warrenty']
            charge = request.POST['serviece charge']
            distance = request.POST['distance']
            
            cus_email = complaint_data.customer_email
            complaint_number = complaint_data.complaint_name
            

            new_report = Work_report(
                complaint_name = complaint_data.complaint_name,
                description = report,
                work_date =today,
                work_time =time,
                serial_number= serial,
                work_status= status,
                warrenty = warrenty,
                serviece_charge = charge,
                travel_distance =  distance,
                complaint_id =complaint_data.id,
                technician_id  = complaint_data.technician_id,
                

            )
            complaint_data.work_status = status
            complaint_data.warrenty = warrenty
            complaint_data.serial = serial
            # print(time,type(time))
            new_report.save()
            complaint_data.save()
           
            
            msg = "Report Added"
            message = "status of your complaint with number "+complaint_number +" is "+ status



        #     send_mail(
        #     'complaint status',
            
        #     message,
        #     settings.EMAIL_HOST_USER,
        #     [cus_email],
        #     fail_silently = False 
        # )


        except Exception as e:
            print(e)
            msg = e
    
    
    return render (request,"add_report.html",context)



def logout(request):
    del request.session['technician']              
    request.session.flush()
    return redirect('Common:home')
@cache_control(no_cache=True, must_revalidate=True,no_store=True)
@auth_technician
def view_work(request,cid):
    name=Technician.objects.get(id=request.session['technician']).tec_name
    complaint_data= Complaint.objects.get(id=cid)
    report_data= Work_report.objects.filter(complaint_id=cid)

    context = {
        'name':name,
        'complaint_data':complaint_data,
        'report_data' :report_data

      }

    return render (request,"view_work_tec.html",context)

@cache_control(no_cache=True, must_revalidate=True,no_store=True)
@auth_technician
def view_my_report(request,cid):
    name=Technician.objects.get(id=request.session['technician']).tec_name
    complaint_data= Complaint.objects.get(id=cid)
    report_data= Work_report.objects.filter(complaint_id=cid)
    context = {
        'name':name,
        'report_data':report_data,
        'complaint_data':complaint_data
    }
    return render (request,"view_my_report.html",context)
