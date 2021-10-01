from django.db import models
import datetime

# Create your models here.
class Ayucare(models.Model):
    productname =models.CharField(max_length=70, blank=False, default='')
    details =models.CharField(max_length=500,blank=False, default='')
    cure =models.CharField(max_length=70,blank=False, default='')
    availability =models.BooleanField(default=False)
    price = models.IntegerField(default=0)
    manufacturedate=models.DateField(default=datetime.date.today)
    expiredate=models.DateField(default=datetime.date.today)


#class User(models.Model):
#    user_name = models.CharField(max_length=70,default='',blank=False)
#    email = models.CharField(max_length=25,default='',blank=False)


#class Purchased(models.Model):
#    user=models.ForeignKey(User,on_delete=models.CASCADE)
#    ayu=models.ForeignKey(Ayucare,on_delete=models.CASCADE)