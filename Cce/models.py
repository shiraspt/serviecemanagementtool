from django.db import models

from Manager.models import Cce, Location, Product_category, Product_models, Technician

# Create your models here.
class Complaint(models.Model):
    
    customer_name = models.CharField(max_length = 50)
    customer_phone1 = models.CharField(max_length = 50)
    customer_phone2 = models.CharField(max_length = 50)
    customer_email = models.CharField(max_length = 50 , default='')
    customer_address = models.CharField(max_length = 500)
    customer_location = models.CharField(max_length = 50)
    location = models.ForeignKey(Location,on_delete = models.CASCADE)
    category_name = models.CharField(max_length = 50)
    category  = models.ForeignKey(Product_category,on_delete = models.CASCADE)
    model_name = models.CharField(max_length = 50)
    model = models.ForeignKey(Product_models,on_delete = models.CASCADE)
    complaint_des = models.CharField(max_length = 50)
    purchase_date = models.DateField( default='')
    complaint_date =models.DateField(default='')
    warrenty = models.CharField(max_length = 50)
    physical_damage = models.CharField(max_length = 50)
    technician_name = models.CharField(max_length = 50)
    technician = models.ForeignKey(Technician,on_delete = models.CASCADE)
    work_status = models.CharField(max_length = 50, default='new')
    remark = models.CharField(max_length = 500, default='')
    cce = models.ForeignKey(Cce,on_delete = models.CASCADE)
    complaint_name = models.CharField(max_length = 50)
    serial = models.CharField(max_length = 50, default = '')

    
   

    class Meta:
        db_table = 'complaint_tb'