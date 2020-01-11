from django.db import models
from django import forms
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    is_consumer = models.BooleanField('consumer status',default=False)
    is_provider = models.BooleanField('provider status',default=False)
    def __str__(self):
        return self.username

class Consumer(models.Model):
    city=(
        ('None','None'),
        ('Mumbai','Mumbai'),
        ('Pune','Pune'),
        ('Hyderabad','Hyderabad')
        )
    have_vehicle=(
        ('Yes','Yes'),
        ('No','No')
        )
    user = models.OneToOneField(User,on_delete = models.CASCADE, primary_key = True)
    have_vehicle = models.CharField(max_length = 10,choices=have_vehicle,default = "")
    city = models.CharField(max_length=20,choices=city,default="")

    def __str__(self):
        return self.user.username + ' - Consumer'

class Provider(models.Model):
    user = models.OneToOneField(User,on_delete = models.CASCADE, primary_key = True)
    business_name = models.CharField(max_length = 100)

    def __str__(self):
        return self.user.username + ' - Provider'

class Vehicle(models.Model):
    name = models.CharField(max_length = 100)
    company = models.CharField(max_length = 100)
    vehicle_range = models.CharField(max_length = 100)
    battery_capacity = models.CharField(max_length = 100)

class ChargingStation(models.Model):
    # One Owner can have multiple charging stations
    owner=models.ForeignKey(Provider,on_delete=models.CASCADE,related_name="ownerof")
    lat = models.DecimalField(max_digits=9,decimal_places=6,blank=True,null=True)
    lng = models.DecimalField(max_digits=9,decimal_places=6,blank=True,null=True)
    no_of_ports = models.IntegerField(default=0)
    fast_dc = models.IntegerField(default=0)
    slow_ac = models.IntegerField(default=0)
    price_kwh = models.DecimalField(max_digits=5,decimal_places=2,default=0.00)
    restroom = models.BooleanField(default= False)
    cctv = models.BooleanField(default = False)
    opening_time = models.TimeField(default = '00:00:00')
    closing_time = models.TimeField(default = '00:00:00')
    image = models.ImageField(null=True, upload_to ='station_pics')

    def __str__(self):
        return str(self.pk) + '.' + self.owner.user.username +" - Charging Station"
    # noofports,fast(dc),slow(ac),restroom,cctv,photos,opening time, closing time 
