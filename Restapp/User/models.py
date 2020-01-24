from django.db import models

# Create your models here.
class Customer(models.Model):
    Name = models.CharField(max_length=50,blank=True)
    Address = models.CharField(max_length=50,blank=True)
    Mobile_No = models.CharField(max_length=10,blank=True)
    Intime=models.TimeField(blank=True,null=True)
    Outtime=models.TimeField(blank=True,null=True)
    Date=models.DateField(blank=True,null=True)
    Day=models.CharField(max_length=50,blank=True)
    Pax=models.IntegerField(null=True)
    Status=models.CharField(max_length=20,default="Active",null=True)