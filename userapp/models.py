from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
import random
from datetime import date
from geopy.geocoders import Nominatim

import datetime
# Create your models here.
due = 0
lat = 0
lng = 0


class User(AbstractUser):
    is_consumer = models.BooleanField('consumer status', default=False)
    is_provider = models.BooleanField('provider status', default=False)

    def __str__(self):
        return self.username


class Consumer(models.Model):
    city = (
        ('None', 'None'),
        ('Mumbai', 'Mumbai'),
        ('Pune', 'Pune'),
        ('Hyderabad', 'Hyderabad')
    )
    have_vehicle = (
        ('Yes', 'Yes'),
        ('No', 'No')
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    have_vehicle = models.CharField(max_length=10, choices=have_vehicle, default="")
    city = models.CharField(max_length=20, choices=city, default="")

    def __str__(self):
        return self.user.username + ' - Consumer'


class Provider(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    business_name = models.CharField(max_length=100)
    image = models.ImageField(blank=True, upload_to='provider_pics')

    def __str__(self):
        return self.user.username + ' - Provider'


def csnames():
    numberList = (["Quick EV Charging", "Snap Charging", "OLA Charge", "Mahindra Electric", "Relaince Charging",
                   "HP Charging", "BP Charging", "Ather Energy", "Power EV", "PowerUP", "EV Charging"])
    return random.choice(numberList)


def generate_lat():
    return round(random.uniform(30.68, 30.76), 6)


def generate_lng():
    return round(random.uniform(76.75, 76.77), 6)


lat = generate_lat()
lng = generate_lng()


def geocity():
    geolocator = Nominatim(user_agent='EV')
    lat = generate_lat()
    lng = generate_lng()
    location = geolocator.reverse(str(lat)+', ' + str(lng), timeout=100)
    if location.raw['address']['city']:
        return location.raw['address']['city']
    return "Lorem ipsum"


def geosub():
    geolocator = Nominatim(user_agent='EV')
    lat = generate_lat()
    lng = generate_lng()
    location = geolocator.reverse(str(lat)+', ' + str(lng), timeout=100)
    if location.raw['address']['suburb']:
        return location.raw['address']['suburb']
    return "Lorem ipsum"


def portscount():
    return random.choice([15, 17, 13, 20, 25, 14, 10])


def fasports():
    return random.choice([4, 5, 6, 7, 4, 2])


def slowports():
    return random.choice([4, 3, 6, 1, 3])


def starttime():
    st = random.choice([12, 11, 10])
    d = datetime.time(st, 00, 00)
    return d


def stoptime():
    sp = random.choice([21, 22, 23, 18, 17])
    t = datetime.time(sp, 00, 00)
    return t


class ChargingStation(models.Model):
    # One Owner can have multiple charging stations
    name = models.CharField(max_length=100, default=csnames)
    city = models.CharField(max_length=100, default="city")
    suburb = models.CharField(max_length=100, default="suburb")
    owner = models.ForeignKey(Provider, on_delete=models.CASCADE, related_name="ownerof")
    lat = models.DecimalField(max_digits=9, decimal_places=6, default=0.00)
    lng = models.DecimalField(max_digits=9, decimal_places=6, default=0.00)
    no_of_ports = models.IntegerField(default=portscount)
    available_ports = models.IntegerField(default=0)
    fast_dc = models.IntegerField(default=fasports)
    created_at = models.DateTimeField(default=timezone.now)
    slow_ac = models.IntegerField(default=slowports)
    price_kwh = models.DecimalField(max_digits=5, decimal_places=2, default=12)
    restroom = models.BooleanField(default=False)
    cctv = models.BooleanField(default=True)
    opening_time = models.TimeField(default=starttime)
    closing_time = models.TimeField(default=stoptime)
    image = models.ImageField(null=True, upload_to='station_pics')

    def __str__(self):
        return str(self.pk) + '. ' + self.owner.user.username + ' ' + self.city

    class Meta():
        ordering = ['-created_at']


def duration():
    return random.randrange(45, 120, 10)


due = duration()


def cost():
    if(45 <= due <= 60):
        return random.randrange(10, 15, 1)
    if(61 <= due <= 80):
        return random.randrange(15, 25, 1)
    if(81 <= due <= 105):
        return random.randrange(25, 35, 1)
    if(106 <= due <= 120):
        return random.randrange(35, 50, 1)


class Vehicle(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    company = models.CharField(max_length=100)
    type4or2 = models.IntegerField()
    horsepower = models.CharField(max_length=100)
    vehicle_range = models.IntegerField()
    ConsumptionPerMin = models.DecimalField(max_digits=9, decimal_places=6)
    battery_type = models.CharField(max_length=100)

    def __str__(self):
        return str(self.pk) + '. ' + self.company


class ChargingStationRecord(models.Model):
    # Records for ChargingStation arrivals of vehicle
    # time start-end, elec reqd
    cs = models.ForeignKey(ChargingStation, on_delete=models.CASCADE)
    consumer = models.ForeignKey(Consumer, on_delete=models.CASCADE, related_name="recordof")
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, related_name="csvehicles")
    duration = models.IntegerField(default=duration)
    elec_consumption = models.IntegerField(default=cost)

    def __str__(self):
        return str(self.pk) + '. ' + self.consumer.user.username


class ChargingStationWeekly(models.Model):
    cs = models.ForeignKey(ChargingStation, on_delete=models.CASCADE)
    d1 = models.IntegerField(default=cost)
    d2 = models.IntegerField(default=cost)
    d3 = models.IntegerField(default=cost)
    d4 = models.IntegerField(default=cost)
    d5 = models.IntegerField(default=cost)
    d6 = models.IntegerField(default=cost)
    d7 = models.IntegerField(default=cost)


def randomvehicles():
    y = random.randrange(00, 15, 2)
    return str(y)


def randomdate():
    start_dt = date.today().replace(day=1, month=1).toordinal()
    end_dt = date.today().toordinal()
    random_day = date.fromordinal(random.randint(start_dt, end_dt))
    return random_day


class CsReport(models.Model):
    cs = models.ForeignKey(ChargingStation, on_delete=models.CASCADE)
    time = models.DateField(default=randomdate)
    t0 = models.IntegerField(default=randomvehicles)
    t1 = models.IntegerField(default=randomvehicles)
    t2 = models.IntegerField(default=randomvehicles)
    t3 = models.IntegerField(default=randomvehicles)
    t4 = models.IntegerField(default=randomvehicles)
    t5 = models.IntegerField(default=randomvehicles)
    t6 = models.IntegerField(default=randomvehicles)
    t7 = models.IntegerField(default=randomvehicles)
    t8 = models.IntegerField(default=randomvehicles)
    t9 = models.IntegerField(default=randomvehicles)
    t10 = models.IntegerField(default=randomvehicles)
    t11 = models.IntegerField(default=randomvehicles)
    t12 = models.IntegerField(default=randomvehicles)
    t13 = models.IntegerField(default=randomvehicles)
    t14 = models.IntegerField(default=randomvehicles)
    t15 = models.IntegerField(default=randomvehicles)
    t16 = models.IntegerField(default=randomvehicles)
    t17 = models.IntegerField(default=randomvehicles)
    t18 = models.IntegerField(default=randomvehicles)
    t19 = models.IntegerField(default=randomvehicles)
    t20 = models.IntegerField(default=randomvehicles)
    t21 = models.IntegerField(default=randomvehicles)
    t22 = models.IntegerField(default=randomvehicles)
    t23 = models.IntegerField(default=randomvehicles)

    def __str__(self):
        return str(self.pk) + '. ' + self.cs.name+' .'+self.cs.city


def city():
    numberList = (["Mumbai", "Pune", "Aurangabad", "Nagpur", "Hyderabad", "Banglore", "Chennai", "Chandigarh"])
    cName = random.choice(numberList)
    return cName


def phone():
    numberList = (["905XXXX876", "7798XXXX67", "876XXXXX12", "234XXXX345",
                   "343XXXX909", "2345XXX436", "3333XXXX23", "6787XXX123"])
    return random.choice(numberList)


def price():
    p = ([12, 32, 9, 10, 12, 20])
    return random.choice(p)


def sub():
    numberList = (["sector 29", "sector 32", "sector 21", "sector 18", "Dwarka"])
    sName = random.choice(numberList)
    return sName


class ChargePooler(models.Model):
    consumer = models.OneToOneField(Consumer, on_delete=models.CASCADE, primary_key=True)
    city = models.CharField(max_length=25, default=city)
    local_area = models.CharField(max_length=25, default=sub)
    ph_no = models.CharField(max_length=13, default=phone)
    cost = models.CharField(max_length=25, default=price)
    normal_port = models.BooleanField(default=True)
    fast_port = models.BooleanField(default=False)


class MaintenanceManDetails(models.Model):
    own = models.OneToOneField(Provider, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    OrgName = models.CharField(max_length=30)
    ph1 = models.CharField(max_length=14)
    ph2 = models.CharField(max_length=14)
    OfficeAdd = models.TextField()
    AreaLocality = models.CharField(max_length=30)
    City = models.CharField(max_length=20)
    CompletedComplaints = models.IntegerField(default=0, blank=True)


class CsMaintenance(models.Model):
    Mm = models.ForeignKey(MaintenanceManDetails, on_delete=models.CASCADE, related_name="jobs")
    csm = models.OneToOneField(Provider, on_delete=models.CASCADE, primary_key=True)
    CsSelect = models.OneToOneField(ChargingStation, on_delete=models.CASCADE)
    ph = models.CharField(max_length=14)
    Problem = models.TextField()


class Support(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="support_requests")
    subject = models.CharField(max_length=20, verbose_name="Title")
    description = models.TextField(max_length=200, verbose_name="Describe issue you are facing")

class UserRecord(models.Model):
    ports = (
        ('Type1', 'Type1'),
        ('Type2', 'Type2'),
        ('Type3', 'Type3')
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="data_by")
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, related_name="vehicles_charged")
    start_time = models.DateTimeField(default=timezone.now)
    stop_time = models.DateTimeField(default=timezone.now)
    port_type = models.CharField(max_length=20, choices=ports, default="")
    lat = models.DecimalField(max_digits=9, decimal_places=6, default=0.00)
    lng = models.DecimalField(max_digits=9, decimal_places=6, default=0.00)


class Survey(models.Model):
    travel_type = (
        ('Personal', 'Personal'),
        ('Ambulance', 'Ambulance'),
        ('Private Authority', 'Private Authority'),
        ('Goverment', 'Goverment'),
        ('Tours and Travel', 'Tours and Travel'),
        ('Goods Carrier', 'Goods Carrier')
    )
    consumer = models.ForeignKey(Consumer, on_delete=models.CASCADE, related_name="consumer_survey")
    charging_time = models.IntegerField(default=0)
    slow_port = models.BooleanField(default=False)
    fast_port = models.BooleanField(default=False)
    vehicle_name = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    means_of_travel =models.CharField(max_length=20, choices=travel_type, default="")
    distance_travelled = models.IntegerField(default=0)
    datetime = models.DateTimeField(default=timezone.now)
