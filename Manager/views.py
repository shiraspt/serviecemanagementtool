from collections import Counter
from datetime import datetime
from itertools import count
from django.shortcuts import render,redirect
from Cce.models import Complaint
from Common.decorators import auth_manager

from Manager.models import Cce, Location, Product_category, Product_models, Technician
from Technician.models import Work_report
from django.views.decorators.cache import cache_control

from django.core.paginator import Paginator
from django.db.models import Q,Count

# Create your views here.
@cache_control(no_cache=True, must_revalidate=True,no_store=True)
@auth_manager
def manager_home(request):
    pending_count = Complaint.objects.filter(work_status='Pending').count
    new_count = Complaint.objects.filter(work_status='new').count
    context ={"pending_count":pending_count,
              "new_count":new_count
              }
    
         

    
    return render (request,"manager_home.html",context)


@cache_control(no_cache=True, must_revalidate=True,no_store=True)
@auth_manager
def add_cce(request):
    msg = ""
    try:
        if request.method =='POST':
            cce_name=request.POST['cce_name']
            cce_mob=request.POST['cce_mob']
            cce_email=request.POST['cce_email']
            cce_age=request.POST['cce_age']
            cce_gender=request.POST['cce_gender']
            cce_address=request.POST['cce_address']
            cce_photo = request.FILES['cce_photo']
            cce_jdate=request.POST['cce_jdate']
            cce_pword=request.POST['cce_pword']


            new_cce = Cce(
                cce_name=cce_name,
                cce_phone=cce_mob,
                cce_email=cce_email,
                cce_age=cce_age,
                cce_gender=cce_gender,
                cce_Address=cce_address,
                cce_photo=cce_photo,
                cce_jdate=cce_jdate,
                cce_password=cce_pword
            )
            new_cce.save()
            msg="New cce added"
            
        
    except Exception as e:
        print(e)
        msg = e

    return render (request,"add_cce.html",{'msg':msg})   
@cache_control(no_cache=True, must_revalidate=True,no_store=True)
@auth_manager
def add_tec(request):
    
    location_list = Location.objects.all()
    msg = ""
    context = {
        'msg':msg,
        'location_list':location_list

    }
    
    try:
        if request.method =='POST':
            tec_name=request.POST['tec_name']
            tec_mob=request.POST['tec_mob']
            tec_email=request.POST['tec_email']
            tec_age=request.POST['tec_age']
            tec_gender=request.POST['tec_gender']
            tec_location_id=int(request.POST['work_location'])
            tec_location = Location.objects.get(id = tec_location_id).location
            tec_loc_id = Location.objects.get(id = tec_location_id).id
            tec_address=request.POST['tec_address']
            tec_photo = request.FILES['tec_photo']
            tec_jdate=request.POST['tec_jdate']
            tec_pword=request.POST['tec_pword']
            # print(tec_location_id)


            new_technician = Technician(
                tec_name=tec_name,
                tec_phone=tec_mob,
                tec_email=tec_email,
                tec_age=tec_age,
                tec_gender=tec_gender,
                tec_location=tec_location,
                tec_Address=tec_address,
                tec_photo=tec_photo,
                tec_jdate=tec_jdate,
                tec_password=tec_pword,
                location_id = tec_loc_id
            )
            new_technician.save()
            # print(request.POST['work_location'])
            msg="New technician added"
            
        
    except Exception as e:
        print(e)
        msg = e

    context = {
        'msg':msg,
        'location_list':location_list

    }
    
    return render (request,"add_tec.html",context)

@cache_control(no_cache=True, must_revalidate=True,no_store=True)
@auth_manager
def update_tech(request,tid):
    msg = ''
    tec_data= Technician.objects.get(id=tid)
    location_list = Location.objects.all()
    context = {
     'tec_data':tec_data,
     'msg':msg,
     'location_list':location_list
 }
    
    if request.method =='POST':
        try:
            tec_name=request.POST['tec_name']
            tec_mob=request.POST['tec_mob']
            tec_email=request.POST['tec_email']
            tec_age=request.POST['tec_age']
            tec_gender=request.POST['tec_gender']
            tec_location_id=request.POST['work_location']
            tec_location=Location.objects.get(id=tec_location_id).location
            tec_address=request.POST['tec_address']
            tec_jdate=request.POST['tec_jdate']
            tec_pword=request.POST['tec_pword']
            # print(tec_location)
           
            # date_object = datetime.strptime(tec_jdate, '%Y-%m-%d').date()
                
            # Technician.objects.get(id=tid).update(tec_name = tec_name)
            #     tec_phone = tec_mob,
            #     tec_email = tec_email,
            #     tec_age = tec_age,
            #     tec_gender = tec_gender,
            #     location_id = tec_location_id,
            #     tec_Address = tec_address,
            #     # tec_jdate = tec_jdate,
            #     tec_password = tec_pword,

            
            new_tech = Technician.objects.get(id=tid)
            
            new_tech.tec_name=tec_name
            
            new_tech.tec_phone=tec_mob
            new_tech.tec_email=tec_email
            new_tech.tec_age=int(tec_age)
            new_tech.tec_gender=tec_gender
            new_tech.tec_location=tec_location
            new_tech.tec_Address=tec_address
            new_tech.location_id = tec_location_id
            if 'tec_photo' in request.FILES:
                new_tech.tec_photo = request.FILES['tec_photo']

            if request.POST['tec_jdate'] != "":
                new_tech.tec_jdate=request.POST['tec_jdate']

            if request.POST['tec_pword'] != "":
                new_tech.tec_password=request.POST['tec_pword']



           
           
           
            new_tech.save()
            tec_data= Technician.objects.get(id=tid)
            return render (request,"tec_profile.html",{'tec_data':tec_data})
            



        except Exception as e:
            print(e)
            msg = e


    else:
        return render (request,"update_tech.html",context)


    


@cache_control(no_cache=True, must_revalidate=True,no_store=True)
@auth_manager
def add_models(request):
 msg=""
 category = Product_category.objects.all()
 context = {
     'category':category,
     'msg':msg
 }
 if request.method =='POST':
     try:
         p_categoryid=request.POST['p_category']
         model_name = request.POST['model_name']
         warrenty = request.POST['warrenty']

         new_model= Product_models(
             model_name = model_name,
             warrenty = warrenty,
             category_id = p_categoryid


         )
         new_model.save()
         msg = "New model added"
     except Exception as e:
         print(e)



         
     


 return render (request,"add_models.html",context)

@cache_control(no_cache=True, must_revalidate=True,no_store=True)
@auth_manager
def work_list(request):
    allworks=Complaint.objects.all().values('id','customer_name','customer_phone1','technician_name','work_status','complaint_name').order_by('-complaint_date','-complaint_name')
    
    # w2 = Complaint.objects.filter(work_status = 'new').values('id')
    
    # allworks= Complaint.objects.all()
    tec_list=Technician.objects.all().values('id','tec_name')
    if  request.method =='POST':
            
            cnumber = request.POST['cnumber']
            if cnumber =="":
                if 'tec' in request.POST and 'status' in request.POST:
                
                  tec_id = request.POST['tec']
                #   print('both selected')
                  allworks= Complaint.objects.filter(technician_id = tec_id, work_status = request.POST['status'])
            
                if 'tec' in request.POST:
      
                 tec_id = request.POST['tec']
                 allworks= Complaint.objects.filter(technician_id = tec_id)


                if 'status' in request.POST:
      
                 status = request.POST['status']
                #  print('stataus selected')
                 allworks= Complaint.objects.filter(work_status = status)


            else:
                search = request.POST['search']
                # print(search)
                if search =='complaint_name':
                 allworks= Complaint.objects.filter(complaint_name__startswith = cnumber)

                if search =='customer_name':
                 allworks= Complaint.objects.filter(customer_name__startswith = cnumber)

                if search =='customer_phone1':
                 allworks= Complaint.objects.filter(customer_phone1__startswith = cnumber)

        
            
            
            # if 'cnumber' in request.POST:
            #     cnumber = request.POST['cnumber']
            #     allworks= Complaint.objects.filter(complaint_name__startswith = cnumber)
            #     if request.POST['cnumber'] =="":
            #         allworks= Complaint.objects.all()


            # status = request.POST['status']

            # if 'tec' in request.POST:
            #     print('tec selected')
            # else:
            #     print('nooo')
            
            # if 'status' in request.POST:
            #     print('status selected')
            # if tec_id == "Select":
            #     if status =="Select":
            #         allworks = Complaint.objects.all()
            #     else: 
            #         allworks = Complaint.objects.filter(work_status = status)

                
            # else:
            #     if  status =="Select":
            #         allworks= Complaint.objects.filter(technician_id = tec_id)
            #     else:
            #         allworks= Complaint.objects.filter(technician_id = tec_id,work_status = status )

                

                
        

    p = Paginator(allworks, 20)
    page_number = request.GET.get('page')
    # print(page_number)
    try:
        page_obj = p.get_page(page_number)
    except Exception as e:
        page_obj = p.page(1) 



    context = {
        'allworks':allworks,
        'tec_list':tec_list,
        'page_obj': page_obj

    }

    
    return render (request,"work_list.html",context)


@cache_control(no_cache=True, must_revalidate=True,no_store=True)
@auth_manager
def view_work(request,cid):
     
     complaint_data= Complaint.objects.get(id=cid)
     report_data= Work_report.objects.filter(complaint_id=cid)
     context = {
         
        'complaint_data':complaint_data,
        'report_data' :report_data

      }

     return render (request,"view_work.html",context)

@cache_control(no_cache=True, must_revalidate=True,no_store=True)

@auth_manager
def view_report(request,cid):
    report_data= Work_report.objects.filter(complaint_id=cid)
    return render (request,"view_report.html",{'report_data':report_data})


@cache_control(no_cache=True, must_revalidate=True,no_store=True)
@auth_manager
def view_tec(request):
    tec_list= Technician.objects.annotate(pend_work = Count('complaint',filter=Q(complaint__work_status='Pending'))).all().values('id','tec_name','tec_phone','tec_location','tec_photo')
    
    # tec_list= Technician.objects.annotate(num_com = Count('complaint__technician_id'))
    # print(tec_list[3].tec_name,tec_list[3].pend_work)
    

    # tec_list1= Technician.objects.all().annotate(pending=Complaint.objects.filter(work_status='new',technician_id=).count)
    # print(tec_list1)
    return render (request,"view_tec.html",{'tec_list':tec_list})


@cache_control(no_cache=True, must_revalidate=True,no_store=True)
@auth_manager
def tec_profile(request,tid):
    tec_data= Technician.objects.get(id=tid)
    return render (request,"tec_profile.html",{'tec_data':tec_data})

# @cache_control(no_cache=True, must_revalidate=True,no_store=True)
# @auth_manager
def logout(request):
    del request.session['manager']              
    request.session.flush()
    return redirect('Common:home')



# def search(request):
    # complaint = Complaint.objects.none()

    # if request.method == 'GET':
    #     search = request.GET.get('searched_data')
    #     if search:
    #         complaint = Complaint.objects.filter(
    #             Q(searched_data__icontains=search)
    #         )
    #     print(complaint,'hqqqqqq')
    # return render(request,'work_list.html',{'data':complaint})