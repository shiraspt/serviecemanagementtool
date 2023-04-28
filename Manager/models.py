from django.db import models

# Create your models here.
class Cce(models.Model):
    cce_name = models.CharField(max_length = 50)
    cce_phone = models.CharField(max_length = 50)
    cce_email = models.CharField(max_length = 50)
    cce_age = models.IntegerField()
    cce_gender = models.CharField(max_length = 50)
    cce_Address = models.CharField(max_length = 500)
    cce_photo = models.ImageField(upload_to='cce/')
    cce_jdate = models.DateField()
    cce_password = models.CharField(max_length = 50)
   

    class Meta:
        db_table = 'cce_tb'

class Location(models.Model):
    location = models.CharField(max_length = 50)
    
    class Meta:
        db_table = 'location_tb'



class Technician(models.Model):
    tec_name = models.CharField(max_length = 50)
    tec_phone = models.CharField(max_length = 50)
    tec_email = models.CharField(max_length = 50)
    tec_age = models.IntegerField()
    tec_gender = models.CharField(max_length = 50)
    tec_Address = models.CharField(max_length = 500)
    tec_location = models.CharField(max_length = 50)
    tec_photo = models.ImageField(upload_to='technician/')
    tec_jdate = models.DateField()
    tec_password = models.CharField(max_length = 50)
    location = models.ForeignKey(Location,on_delete = models.CASCADE, default='')
    

    class Meta:
        db_table = 'technician_tb'




class Product_category(models.Model):
    category = models.CharField(max_length = 50)
    
    class Meta:
        db_table = 'productcategory_tb'


class Product_models(models.Model):
    category  = models.ForeignKey(Product_category,on_delete = models.CASCADE)
    model_name = models.CharField(max_length = 50)
    warrenty = models.IntegerField()
    
    class Meta:
        db_table = 'productmodels_tb'
