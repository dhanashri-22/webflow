from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=200,null= True)
    email = models.CharField(max_length=200,null= True)
    mobile = models.CharField(max_length=200,null= True)