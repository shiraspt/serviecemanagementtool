from datetime import date
import datetime
import random
from django.http import JsonResponse
from django.shortcuts import render,redirect
from Cce.models import Complaint
from django.core.mail import send_mail
from Common.decorators import auth_cce
from Manager.models import Cce, Location, Product_category, Product_models, Technician
from smt import settings
from datetime import datetime
from django.core.paginator import Paginator
from django.views.decorators.cache import cache_control
# Create your views here.
@cache_control(no_cache=True, must_revalidate=True,no_store=True)
@auth_cce
def cce_home(request):
    cce_details= Cce.objects.filter(id=request.session['cce'])
    
    
    
    return render (request,"cce_home.html",{'cce_details':cce_details})


@cache_control(no_cache=True, must_revalidate=True,no_store=True)
@auth_cce
def register_work(request):
    
    
    msg = ""
    cce_data = Cce.objects.get(id=request.session['cce'])
    location_list = Location.objects.all()
    category_list = Product_category.objects.all()
    model_list = Product_models.objects.all()
    context={
        'location_list':location_list,
        'msg':msg,
        'category_list':category_list,
        'model_list':model_list
    } 
    if request.method =='POST':
        try:
            
            cus_name=request.POST['customer_name']
            cus_phone1=request.POST['customer_phone']
            cus_phone2=request.POST['customer_phone']
            cus_email=request.POST['customer_email']
            cus_address=request.POST['customer_address']
            work_location_id = int(request.POST['work_location'])
            product_category_id = int(request.POST['product_category'])
            product_model_id = int(request.POST['product_model'])
            complaint = request.POST['complaint']
            purchase_date = request.POST['purchase date']
            location = Location.objects.get(id=work_location_id)



            productcategory = Product_category.objects.get(id=product_category_id)
            model=Product_models.objects.get(id=product_model_id)
            location_id = location.id
            location_name = location.location
            productcategory_id = productcategory.id
            productcategory_name = productcategory.category
            model_id = model.id
            model_name = model.model_name



            technicians = Technician.objects.filter(location_id=location_id)
            technician = random.choice(technicians)
            technician_id = technician.id
            technician_name = technician.tec_name
            # warrenty_per = model.warrenty
            warrenty = "in warrenty"
            physical_damage= "no"
            status ='new'
            # pd = datetime.strptime(purchas_date, '%yyyy-%mm-%dd')
            day = date.today()
            # t=day - pd
            y = day.strftime("%Y")
            m= day.strftime("%m")
            d= day.strftime("%d")
            today_works = Complaint.objects.filter(complaint_date = day).count()
            w = today_works+1
            c=str(w).zfill(3)
            complaint_number= d+m+y[2]+y[3]+c
           
          
            date_string =purchase_date
            # date1 = datetime.strptime(purchase_date, '%d/%m/%Y')
            date_object = datetime.strptime(date_string, '%Y-%m-%d').date()
           
            d= day-date_object
          


            
            complaint_data = {'cus_name':cus_name,'cus_phone1':cus_phone1,'cus_phone2':cus_phone2,'cus_email':cus_email,'cus_address':cus_address,'location_name':location_name,'product_category_id':product_category_id,'product_model_id':product_model_id,'complaint':complaint,'purchase_date':purchase_date,'productcategory_name':productcategory_name,'model_name':model_name,'technician_name':technician_name,'warrenty':warrenty,'physical_damage':physical_damage,'day':day,'complaint_number':complaint_number,'status':status}
            

            new_work = Complaint(
                customer_name = cus_name,
                customer_phone1 = cus_phone1,
                customer_phone2 = cus_phone2,
                customer_email = cus_email,
                customer_address = cus_address,
                customer_location = location_name,
                location_id = location_id,
                category_name = productcategory_name,
                category_id  = productcategory_id,
                model_name =model_name,
                model_id = model_id,
                complaint_des = complaint,
                purchase_date = purchase_date,
                complaint_date =day,
                warrenty = warrenty,
                physical_damage = physical_damage,
                technician_name = technician_name,
                technician_id = technician_id,
                
                cce_id = cce_data.id,
                complaint_name = complaint_number,
            )
           
            new_work.save()
            
            
            message = "Your complaint registerd with complaint number " +complaint_number+".Our technician will contact you soon"
            msg = "Work assigned to " + technician_name + " with complaint number " + complaint_number
          
            
    

        #     send_mail(
        #     'complaint registerd',
            
        #     message,
        #     settings.EMAIL_HOST_USER,
        #     [cus_email],
        #     fail_silently = False 
        # )


            return render (request,"added_data.html",{'complaint_data':complaint_data})

        except Exception as e:
            print(e)
                 

        
    else:
        return render (request,"register_work.html",context)


        

     
    
    
    


def logout(request):
    del request.session['cce']              
    request.session.flush()
    return redirect('Common:home')


def model_select(request):
   
    category_id = request.POST['product_category']
    models = Product_models.objects.filter(category_id = category_id)
    modl=[{'id':i.id,'name':i.model_name} for i in models]

    return JsonResponse({'models':modl})


@cache_control(no_cache=True, must_revalidate=True,no_store=True)
@auth_cce
def added_data(request,cid):
     
     complaint_data=Complaint.objects.get(id = cid)
    #  print(complaint_data.id)
     return render (request,"added_data.html",{ 'complaint_data': complaint_data})


@cache_control(no_cache=True, must_revalidate=True,no_store=True)
@auth_cce
def update_complaint(request,cid):

    complaint_data = Complaint.objects.get(id = cid)
    location_list = Location.objects.all()
    category_list = Product_category.objects.all()
    model_list = Product_models.objects.all()
    technician_list = Technician.objects.all()

    # print (complaint_data.purchase_date)
    

    datetimeobject = complaint_data.purchase_date
    date_object  = datetimeobject.strftime('%m-%d-%Y')
    datetimeobject1 = datetimeobject.strftime("%Y-%m-%d")
    # print(datetimeobject1,type(datetimeobject1))
    # print(datetimeobject1,type(datetimeobject1))
    
   
    # print((type(new_format)),"6666666666")
    context = {
        'complaint_data':complaint_data,
        'datetimeobject1' : datetimeobject1,
        'location_list' : location_list,
        'category_list' : category_list,
        'model_list' : model_list,
        'technician_list' : technician_list
    }


    
    if request.method == 'POST':
     try:
         
         customer_name=request.POST['customer_name']
         customer_phone=request.POST['customer_phone']
         customer_phone2=request.POST['customer_phone2']
         customer_email=request.POST['customer_email']
         customer_address=request.POST['customer_address']
         work_location_id=request.POST['work_location']
         product_category_id=int(request.POST['product_category'])
         product_model_id=int(request.POST['product_model'])
         complaint=request.POST['complaint']
         serial=request.POST['serial']
         remark=request.POST['remark']
         purchase_date = request.POST['purchase date']
         location_id = Location.objects.get(id = work_location_id ).id
         work_location = Location.objects.get(id = work_location_id ).location
         tech_id=int(request.POST['technician'])
         technician =  Technician.objects.get(id = tech_id )
         
         category_name = Product_category.objects.get(id = product_category_id ).category
         model = Product_models.objects.get(id = product_model_id).model_name






         new_complaint = Complaint.objects.get(id = cid)

         new_complaint.customer_name = customer_name
         new_complaint.customer_phone1 = customer_phone
         new_complaint.customer_phone2 = customer_phone2
         new_complaint. customer_email = customer_email
         new_complaint.customer_address = customer_address
         new_complaint.customer_location = work_location
         
         new_complaint.complaint_des = complaint
         new_complaint.purchase_date = purchase_date
         new_complaint.category_id = product_category_id
         new_complaint.location_id = location_id
         new_complaint.model_id = product_model_id
         
         new_complaint.technician_name = technician.tec_name
         new_complaint.technician_id = technician.id
         new_complaint.remark = remark
         new_complaint.category_name = category_name
         new_complaint.model_name = model
         new_complaint.serial = serial
        
         new_complaint.save()
         complaint_data = Complaint.objects.get(id = cid)
         return render (request,"view_complaint.html",{'complaint_data':complaint_data})


         
     
     except Exception as e:
      
      print(e)
    
    else:

        return render (request,"update_complaint.html",context)

    
@cache_control(no_cache=True, must_revalidate=True,no_store=True)
@auth_cce
def complaint_list(request):
    # cce_details= Cce.objects.filter(id=request.session['cce'])
    allworks = Complaint.objects.all().order_by('-complaint_date','-complaint_name').values('id','customer_name','customer_phone1','technician_name','work_status','complaint_name')
    p = Paginator(allworks, 20)
    page_number = request.GET.get('page')
    # print(page_number)
    try:
        page_obj = p.get_page(page_number)
    except Exception as e:
        page_obj = p.page(1) 

    context = {
        'allworks':allworks,
        'page_obj':page_obj
    }

    
    
    
    return render (request,"complaint_list.html",context)


@cache_control(no_cache=True, must_revalidate=True,no_store=True)
@auth_cce
def view_complaint(request,cid):
    # cce_details= Cce.objects.filter(id=request.session['cce'])
    complaint_data = Complaint.objects.get(id = cid)

    
    
    
    return render (request,"view_complaint.html",{'complaint_data':complaint_data})



def tec_select(request):
   
    location_id = int(request.POST['location'])
    
    technicians = Technician.objects.filter(location_id = location_id).values('id','tec_name')
    tec=[{'id':i.id,'name':i.tec_name} for i in technicians]

    return JsonResponse({'tec':tec})