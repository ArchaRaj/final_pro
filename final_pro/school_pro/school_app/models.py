from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Option(models.Model):
    opt=models.CharField(max_length=100)
class Table1(models.Model):
    name=models.CharField(max_length=250)
    dob=models.CharField(max_length=250)
    age=models.CharField(max_length=10)
    gender=models.CharField(max_length=10)
    phone=models.CharField(max_length=100)
    email=models.EmailField(max_length=254)
    address=models.CharField(max_length=210)
    department=models.CharField(max_length=100)
    course=models.CharField(max_length=100)
    purpose=models.CharField(max_length=250)
    material=models.ManyToManyField(Option)
    login_person=models.ForeignKey(User,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.name