import datetime
import django
from django.db import models
# Create your models here.


class Person(models.Model):
    Name = models.CharField(max_length=64)
    Surname = models.CharField(max_length=64)
    Sex = models.CharField(max_length=1)

class Customer(models.Model):
    id = models.BigAutoField(primary_key=True, editable=False)
    Name = models.CharField(max_length=64,blank=True)
    Gender = models.CharField(max_length=10,blank=True)
    Age = models.IntegerField(blank=True)
    BirthDate = models.DateTimeField(default=django.utils.timezone.now,blank=True)
    Driving_License = models.IntegerField(blank=True)
    Region_Code = models.FloatField(blank=True)
    Previously_Insured = models.IntegerField(blank=True)
    Vehicle_Age = models.IntegerField(blank=True)
    Vehicle_Damage = models.CharField(max_length=10,blank=True)
    Annual_Premium = models.IntegerField(blank=True)
    Policy_Sales_Channel = models.IntegerField(blank=True)
    Vintage =  models.IntegerField(blank=True)
    

