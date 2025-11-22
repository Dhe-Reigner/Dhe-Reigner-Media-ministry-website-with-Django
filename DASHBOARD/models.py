from django.db import models
from django.contrib.auth.models import User
import datetime


# Create your models here.
class Employee(models.Model):
    id_number = models.IntegerField(primary_key=True)
    employee_image = models.ImageField(upload_to='Employee_images/')
    name = models.CharField(max_length=100)
    id_image = models.ImageField(upload_to='ID_images')
    gender = models.CharField(max_length=10,choices=[('Male','Male'),('Female','Female')],null=True,blank=True)
    date = models.DateField(default=datetime.datetime.today)
    mobile_number = models.CharField(max_length=100)
    assignment = models.TextField(max_length=200,default=True)

    def __str__(self):
        return f"Employee: {self.id_number} {self.employee_image} {self.name} {self.id_image} {self.gender} {self.date} {self.mobile_number} {self.assignment}"

class Farm(models.Model):
    farm_number = models.IntegerField(primary_key=True)
    farm_image = models.ImageField(upload_to='Farm_images/')
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=1000,default=True)


    def __str__(self):
        return f"Farm: {self.farm_number} {self.farm_image} {self.name}"
