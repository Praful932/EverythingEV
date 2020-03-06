from django.db import models
from django import forms
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
import random
from random import randrange
from datetime import date
from geopy.geocoders import Nominatim

import datetime 
# Create your models here.

due=0
lat=0
lng=0
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
    image = models.ImageField(blank=True, upload_to ='provider_pics')
    def __str__(self):
        return self.user.username + ' - Provider'


def csnames():
    numberList = (["Quick EV Charging", "Snap Charging","OLA Charge","Mahindra Electric","Relaince Charging","HP Charging","BP Charging","Ather Energy","Power EV","PowerUP","EV Charging"])
    return random.choice(numberList)

def generate_lat():
    return round(random.uniform(30.68,30.76),6)

def generate_lng():
    return round(random.uniform(76.75,76.77),6)
lat=generate_lat()
lng=generate_lng()
def geocity():
    geolocator = Nominatim(user_agent = 'EV')
    lat=generate_lat()
    lng=generate_lng()
    location = geolocator.reverse(str(lat)+', ' + str(lng),timeout=100)
    return location.raw['address']['city']
def geosub():
    geolocator = Nominatim(user_agent = 'EV')
    lat=generate_lat()
    lng=generate_lng()
    location = geolocator.reverse(str(lat)+', ' + str(lng),timeout=100)
    return location.raw['address']['suburb']
    
def portscount():
    return random.choice([15,17,13,20,25,14,10])

def fasports():
    return random.choice([4,5,6,7,4,2])
def slowports():
    return random.choice([4,3,6,1,3])
def starttime():
    st=random.choice([12,11,10])
    d=datetime.time(st,00,00)
    return d
def stoptime():
    sp=random.choice([21,22,23,18,17])
    t=datetime.time(sp,00,00)
    return t
class ChargingStation(models.Model):
    # One Owner can have multiple charging stations
    name = models.CharField(max_length = 100,default=csnames)
    city = models.CharField(max_length = 100, default=geocity)
    suburb = models.CharField(max_length = 100,default=geosub)
    owner=models.ForeignKey(Provider,on_delete=models.CASCADE,related_name="ownerof")
    lat = models.DecimalField(max_digits=9,decimal_places=6,default=lat)
    lng = models.DecimalField(max_digits=9,decimal_places=6,default=lng)
    no_of_ports = models.IntegerField(default=portscount)
    available_ports = models.IntegerField(default=0)
    fast_dc = models.IntegerField(default=fasports)
    created_at=models.DateTimeField(default = timezone.now)
    slow_ac = models.IntegerField(default=slowports)
    price_kwh = models.DecimalField(max_digits=5,decimal_places=2,default=12)
    restroom = models.BooleanField(default= False)
    cctv = models.BooleanField(default = True)
    opening_time = models.TimeField(default = starttime)
    closing_time = models.TimeField(default = stoptime)
    image = models.ImageField(null=True, upload_to ='station_pics')

    def __str__(self):
        return str(self.pk) + '. ' +  self.owner.user.username + ' ' + self.city
    # noofports,fast(dc),slow(ac),restroom,cctv,photos,opening time, closing time 


def duration():
    return random.randrange(45,120,10)
    
due=duration()
def cost():
    if(45<=due<=60):
        return random.randrange(10,15,1)
    if(61<=due<=80):
        return random.randrange(15,25,1)
    if(81<=due<=105):
        return random.randrange(25,35,1)
    if(106<=due<=120):
        return random.randrange(35,50,1)
class ChargingStationRecord(models.Model):
    # Records for ChargingStation arrivals of vehicle
    # time start-end, elec reqd,
    cs = models.OneToOneField(ChargingStation, on_delete = models.CASCADE, primary_key=True)
    # vehicle =models.OneToOne(Vehicle,on_delete=models.CASCADE,related_name="csvehicles")
    # starttime = models.TimeField(default = '00:00:00')
    # stoptime = models.TimeField(default = '00:00:00')
    # duration = IntegerField(default=0)
    elec_kwh = models.DecimalField(max_digits=9,decimal_places=6,default=cost)

class Vehicle(models.Model):
    company=models.CharField(max_length=100)
    type4or2=models.IntegerField()
    horsepower=models.CharField(max_length=100)
    vehicle_range=models.IntegerField()
    price=models.DecimalField(max_digits=9,decimal_places=6)
    battery_type=models.CharField(max_length=100)


def randomvehicles():
    y=random.randrange (00,15, 2)
    return str(y)  

def randomdate():
    start_dt = date.today().replace(day=1, month=1).toordinal()
    end_dt = date.today().toordinal()
    random_day = date.fromordinal(random.randint(start_dt, end_dt))
    return random_day

class CsReport(models.Model):
    cs = models.OneToOneField(ChargingStation, on_delete = models.CASCADE, primary_key=True)
    time=models.DateField(default = randomdate )
    t0=models.IntegerField(default=randomvehicles)
    t1=models.IntegerField(default=randomvehicles)
    t2=models.IntegerField(default=randomvehicles)
    t3=models.IntegerField(default=randomvehicles)
    t4=models.IntegerField(default=randomvehicles)
    t5=models.IntegerField(default=randomvehicles)
    t6=models.IntegerField(default=randomvehicles)
    t7=models.IntegerField(default=randomvehicles)
    t8=models.IntegerField(default=randomvehicles)
    t9=models.IntegerField(default=randomvehicles)
    t10=models.IntegerField(default=randomvehicles)
    t11=models.IntegerField(default=randomvehicles)
    t12=models.IntegerField(default=randomvehicles)
    t13=models.IntegerField(default=randomvehicles)    
    t14=models.IntegerField(default=randomvehicles)
    t15=models.IntegerField(default=randomvehicles)
    t16=models.IntegerField(default=randomvehicles)
    t17=models.IntegerField(default=randomvehicles)
    t18=models.IntegerField(default=randomvehicles)
    t19=models.IntegerField(default=randomvehicles)
    t20=models.IntegerField(default=randomvehicles)
    t21=models.IntegerField(default=randomvehicles)
    t22=models.IntegerField(default=randomvehicles)
    t23=models.IntegerField(default=randomvehicles)
    t24=models.IntegerField(default=randomvehicles)

    def __str__(self):
        return str(self.pk) + '. ' + self.cs.name+' .'+self.cs.city
