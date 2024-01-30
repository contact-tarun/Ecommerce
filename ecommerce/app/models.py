from django.db import models

class Registration(models.Model):
    fname=models.CharField(max_length=50)
    lname=models.CharField(max_length=50)
    email=models.EmailField()
    contact=models.IntegerField(max_length=10)
    uname=models.CharField(max_length=12)
    password=models.CharField(max_length=12)
    cpassword=models.CharField(max_length=12)
