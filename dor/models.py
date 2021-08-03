from django.db import models

# Create your models here.

class Contactus(models.Model):
    mail=models.EmailField(max_length=40)
    Name=models.CharField(max_length=40)
    Issue=models.CharField(max_length=100)
    Whatshap=models.IntegerField()
    Contact=models.IntegerField()
    State=models.CharField(max_length=40)

class Internship(models.Model):
    FirstName=models.CharField(max_length=30)
    LastName=models.CharField(max_length=30)
    Email=models.EmailField(max_length=30)
    Contactno=models.IntegerField()
    College=models.CharField(max_length=40)
    InternField=models.CharField(max_length=30)

