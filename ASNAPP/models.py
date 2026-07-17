from django.db import models

# Create your models here.
class ASN(models.Model):    
    name = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=255)

class Admin(models.Model):
    username = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=255)
   
class company(models.Model):
    name = models.CharField(max_length=20, unique=True)
    description = models.TextField()

class product(models.Model):
    com=models.ForeignKey(company, on_delete=models.CASCADE)
    name = models.CharField(max_length=20, unique=True)
    
class specifications(models.Model):
    prod=models.ForeignKey(product, on_delete=models.CASCADE)
    name = models.TextField()
    value = models.TextField()
    