from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request,"userapp/index.html")

def stations(request):
    return render(request, "userapp/stations.html")

def vehicledata_c(request):
    return render(request, "userapp/vehicledata_c.html")
def vehicledata_p(request):
    return render(request, "userapp/vehicledata_p.html")