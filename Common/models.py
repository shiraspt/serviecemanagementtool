from django.db import models

# Create your models here.
class Manager(models.Model):
    manager_name = models.CharField(max_length = 50)
    manager_phone = models.CharField(max_length = 50)
    manager_email = models.CharField(max_length = 50)
    
    manager_password = models.CharField(max_length = 50)
   

    class Meta:
        db_table = 'manager_tb'
