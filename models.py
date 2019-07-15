from django.db import models
from choice import quali,clg,gent,spcl,day,month,year,tech,posi,location,ex
from datetime import datetime



class datas(models.Model):

    college=models.CharField(max_length=20,choices=clg,default='')
    name=models.CharField(max_length=20,default='')
    qualification=models.CharField(max_length=20,choices=quali,default='')
    specialization=models.CharField(max_length=20,choices=spcl,default='')
    arrears=models.IntegerField(default='')
    area_of_interest=models.CharField(max_length=25,default='')
    contact=models.CharField(max_length=20,default='')
    address=models.TextField(max_length=20,default='')
    email=models.EmailField(max_length=254,default='')
    # gender=models.CharField(max_length=5,choices=gent,default='')
    day=models.CharField(max_length=3,choices=day,default='')
    month=models.CharField(max_length=20,choices=month,default='')
    year=models.CharField(max_length=20,choices=year,default='')
    photo=models.ImageField(upload_to='volt/proof/',default='')
    proof=models.FileField(upload_to='volt/photos/',default='')
    user=models.CharField(null=False,max_length=25,default='')
    passid=models.CharField(max_length=20,default='')
    confirm_passid=models.CharField(max_length=20,default='')

    def __str__(self):
        return self.user

class fresher(models.Model):
    name=models.CharField(max_length=20,default='')
    degree=models.CharField(max_length=20,choices=quali,default='')
    year_of_pass=models.IntegerField(default='')
    skill=models.CharField(max_length=20,choices=tech,default='')
    mobile=models.CharField(max_length=20,default='')
    present_address=models.TextField(max_length=20,default='')
    permenant_address=models.TextField(max_length=20,default='')
    # gender=models.CharField(max_length=5,choices=gent,default='')
    day = models.CharField(max_length=3, choices=day, default='')
    month = models.CharField(max_length=20, choices=month, default='')
    year = models.CharField(max_length=20, choices=year, default='')
    email=models.EmailField(max_length=220,default='')
    passid=models.CharField(max_length=20,default='')
    #

    def __str__(self):
        return  self.email


class experience(models.Model):
    name=models.CharField(max_length=20,default='')
    domain=models.CharField(max_length=40,default='')
    position= models.CharField(max_length=40, choices=posi, default='')
    notice=models.CharField(max_length=40,default='')
    last_ctc=models.IntegerField(default='')
    expext_ctc=models.IntegerField(default='')
    reason= models.CharField(max_length=200, choices=posi, default='')
    mobile=models.CharField(max_length=20,default='')
    location= models.CharField(max_length=20, choices=location, default='')
    experience= models.CharField(max_length=20, choices=ex, default='')
    skill=models.CharField(max_length=20,choices=tech,default='')
    qualification=models.CharField(max_length=20,choices=quali,default='')
    user= models.CharField(null=False, max_length=25, default='')
    passid= models.CharField(max_length=20, default='')

    def __str__(self):
        return  self.user

class forget_admin(models.Model):
    email = models.EmailField(max_length=220, default='')
    passid = models.CharField(max_length=20, default='')

    def __str__(self):
        return self.email

class datab(models.Model):
    mark=models.IntegerField(default='')

    def __int__(self):
        return self.mark