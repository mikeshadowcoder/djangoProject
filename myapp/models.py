from django.db import models


# Create your models here.
class Employee(models.Model):  
    firstname = models.CharField(max_length=100)  
    lastname = models.CharField(max_length=100) 
    email = models.EmailField()  
    contact = models.CharField(max_length=15) 
    country = models.CharField(max_length=100) 
    city= models.CharField(max_length=100) 
   
    class Meta:  
        db_table = "tblempinfo"