from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    is_consumer = models.BooleanField('consumer status',default=False)
    is_provider = models.BooleanField('provider status',default=False)
    def __str__(self):
        return self.username

class Consumer(models.Model):
    user = models.OneToOneField(User,on_delete = models.CASCADE, primary_key = True)
    have_vehicle = models.BooleanField('Have Vehicle',default = False)

class Provider(models.Model):
    user = models.OneToOneField(User,on_delete = models.CASCADE, primary_key = True)
    lat = models.DecimalField(max_digits=9,decimal_places=6,blank=True,null=True)
    lng = models.DecimalField(max_digits=9,decimal_places=6,blank=True,null=True)
    business_name = models.CharField(max_length = 100)

class Vehicle(models.Model):
    name = models.CharField(max_length = 100)
    company = models.CharField(max_length = 100)
    range = models.CharField(max_length = 100)
    battery_capacity = models.CharField(max_length = 100)
    