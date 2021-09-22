from django.db import models

# Create your models here.
class Ayucare(models.Model):
    productname =models.CharField(max_length=70, blank=False, default='')
    usedfor =models.CharField(max_length=70,blank=False, default='')
    availability =models.BooleanField(default=False)
    price = models.IntegerField(default=0)

