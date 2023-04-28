from django.db import models
from Cce.models import Complaint

from Manager.models import Technician

# Create your models here.
class Work_report(models.Model):
    complaint_name = models.CharField(max_length = 50)
    description = models.CharField(max_length = 1000, default='')
    work_date = models.DateField( default='')
    work_time = models.TimeField( default='')
    serial_number = models.CharField(max_length = 50,default='')
    warrenty = models.CharField(max_length = 50)
    work_status  = models.CharField(max_length = 50)
    serviece_charge = models.FloatField(default='')
    travel_distance = models.FloatField(max_length = 50,default='')
    complaint = models.ForeignKey(Complaint,on_delete = models.CASCADE)
    technician = models.ForeignKey(Technician,on_delete = models.CASCADE)
    class Meta:
        db_table = 'workreport_tb'




    
    

    
   

    