from django.shortcuts import render, redirect,get_object_or_404
from django.views.generic import DetailView, ListView, UpdateView, DeleteView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django import forms
from django.core.paginator import Paginator
from geopy.geocoders import Nominatim
from django.urls import reverse_lazy
from django.db.models import Case, When
from django.http import HttpResponse
from userapp.forms import UserSignUpForm, ConsumerSignUpForm, ProviderSignUpForm, UserUpdateForm, ChargingStationForm
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from userapp.models import User, Consumer, Provider, Vehicle, ChargingStation, ChargingStationRecord, CsReport, ChargingStationWeekly, ChargePooler,MaintenanceManDetails,CsMaintenance
from urllib.request import urlopen
from django.http import JsonResponse
import json
import random
import math

# Create your views here.

import math

def get_distance(lat_1, lng_1, lat_2, lng_2): 
    d_lat = lat_2 - lat_1
    d_lng = lng_2 - lng_1 

    temp = (  
         math.sin(d_lat / 2) ** 2 
       + math.cos(lat_1) 
       * math.cos(lat_2) 
       * math.sin(d_lng / 2) ** 2
    )

    return 6373.0 * (2 * math.atan2(math.sqrt(temp), math.sqrt(1 - temp)))

def index(request):
    if request.user.is_authenticated :
        try:
            if Consumer.objects.get(user =  request.user):
                pass
        except:
            try:
                if Provider.objects.get(user =  request.user):
                    pass
            except:
                return redirect('registerConsumerSocial')
    return render(request,"userapp/index.html")

def registerConsumerSocial(request):
    if request.method == 'POST':
        consumerform = ConsumerSignUpForm(request.POST)
        if consumerform.is_valid():
            new_user = User.objects.get(username = request.user.username)
            new_user.is_consumer = True
            consumer = consumerform.save(commit = False)
            consumer.user = new_user
            new_user.save()
            consumerform.save()
            return redirect('index')
    else:
        consumerform = ConsumerSignUpForm()
    context = {
        'consumerform' : consumerform
    }
    return render(request, "userapp/registerConsumer.html", context = context)
def register(request):
    return render(request,"userapp/registration_page.html")

def registerConsumer(request):
    if request.user.is_authenticated:
        logout(request)
    if request.method == 'POST':
        signupform = UserSignUpForm(request.POST)
        consumerform = ConsumerSignUpForm(request.POST)
        if signupform.is_valid() and consumerform.is_valid():
            username = signupform.cleaned_data.get('username')
            new_user = signupform.save(commit = False)
            new_user.is_consumer = True
            new_user = signupform.save()
            login(request,new_user,backend='django.contrib.auth.backends.ModelBackend')
            consumer = consumerform.save(commit = False)
            consumer.user = new_user
            consumerform.save()
            return redirect('index')
    else:
        signupform = UserSignUpForm()
        consumerform = ConsumerSignUpForm()
    context = {
        'signupform' : signupform,
        'consumerform' : consumerform
    }
    return render(request, "userapp/registerConsumer.html", context = context)

def registerProvider(request):
    if request.user.is_authenticated:
        logout(request)
    if request.method == 'POST':
        signupform = UserSignUpForm(request.POST, request.FILES)
        providerform = ProviderSignUpForm(request.POST)
        if signupform.is_valid() and providerform.is_valid():
            username = signupform.cleaned_data.get('username')
            new_user = signupform.save(commit = False)
            new_user.is_provider = True
            new_user = signupform.save()
            login(request,new_user,backend='django.contrib.auth.backends.ModelBackend')
            consumer = providerform.save(commit = False)
            consumer.user = new_user
            providerform.save()
            return redirect('index')
    else:
        signupform = UserSignUpForm()
        providerform = ProviderSignUpForm()
    context = {
        'signupform' : signupform,
        'providerform' : providerform
    }
    return render(request, "userapp/registerProvider.html", context = context)

def logoutf(request):
    # Check if user is logged in if not redirect to login page
    if request.user.is_authenticated:
        # username = request.user.username
        logout(request)
        return redirect('index')
    return redirect('login')

@login_required
def UpdateProfile(request):
    if request.method == "GET":
        if request.user.is_consumer:
            userform = UserUpdateForm(instance=request.user)
            fieldform = ConsumerSignUpForm(instance=request.user.consumer)
        else:
            userform = UserUpdateForm(instance=request.user)
            fieldform = ProviderSignUpForm(instance=request.user.provider)
        context = {
            'userform': userform,
            'fieldform': fieldform
        }
    else:
        if request.user.is_consumer:
            userform = UserUpdateForm(request.POST, instance=request.user)
            fieldform = ConsumerSignUpForm(
                request.POST, instance=request.user.consumer)
        else:
            userform = UserUpdateForm(request.POST, instance=request.user)
            fieldform = ProviderSignUpForm(
                request.POST, instance=request.user.provider)
        if userform.is_valid() and fieldform.is_valid():
            userform.save()
            fieldform.save()
            return redirect('index')
    return render(request, "userapp/updateprofile.html", context=context)

# ChargingStation
@login_required
def CS(request):
    if request.user.is_consumer:
        return redirect('Charging-Station-CLV')
    if request.user.is_provider:
        # Redirect to Charging Station Provider ListView
        return redirect('Charging-Station-PLV')
    
@login_required
def AddChargingStation(request):
    if request.user.is_consumer:
        return redirect('index')
    else:
        if request.method == 'POST':
            stationform = ChargingStationForm(request.POST, request.FILES)
            if stationform.is_valid():
                ob = stationform.save(commit = False)
                provider = Provider.objects.get(user=request.user)
                ob.owner = provider
                lat = stationform.cleaned_data['lat']
                lng = stationform.cleaned_data['lng']
                geolocator = Nominatim(user_agent = 'EV')
                location = geolocator.reverse(str(lat)+', ' + str(lng))
                try:
                        ob.city = location.raw['address']['city']
                except:
                        ob.city = location.raw['address']['state_district']
                try:
                    ob.suburb = location.raw['address']['suburb']
                except:
                    try:
                        ob.suburb = location.raw['address']['county']
                    except:
                        ob.suburb = location.raw['address']['town']
                stationform.save()
                return redirect('Charging-Station-PLV')
        else:
            stationform = ChargingStationForm()
            stationform.fields['lat'].widget = forms.HiddenInput()
            stationform.fields['lng'].widget = forms.HiddenInput()
    context = {
        'stationform' : stationform
    }
    return render(request, "userapp/add_charging_station.html", context = context)

class ChargingStationProviderListView(LoginRequiredMixin,UserPassesTestMixin,ListView):
    model = ChargingStation
    template_name = 'userapp/provider_charging_stations.html'
    ordering = ['-created_at']
    context_object_name = 'cslist'
    paginate_by = 3

    def test_func(self):
        if self.request.user.is_provider:
            return True
        return False
    
    def get_queryset(self):
        current_provider = Provider.objects.get(user=self.request.user)
        return ChargingStation.objects.filter(owner=current_provider)

class ChargingStationProviderDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = ChargingStation
    success_url = reverse_lazy('Charging-Station-PLV')

    # Check if current user is author of the post
    def test_func(self):
        cs = self.get_object()
        if self.request.user.is_provider and (cs.owner.user == self.request.user):
            return True
        return False

@login_required
def ChargingStationConsumer(request):
    if request.user.is_consumer:
        url = 'http://ipinfo.io/json'
        response = urlopen(url)
        data = json.load(response)
        # print(data)
        # Get User location(lat & lng)
        lat_user = math.radians(float(data['loc'].split(',')[0]))
        lng_user = math.radians(float(data['loc'].split(',')[1]))
        cslist = ChargingStation.objects.all()
        distid_list = []
        for cs in cslist:
            # Convert degree to radians
            lat_cs, lng_cs= map(math.radians, [float(cs.lat), float(cs.lng)])
            distance = get_distance(lat_user,lng_user,lat_cs,lng_cs)
            distid_list.append([distance,cs.pk])
        distid_list.sort()
        # Sorted id of Charging Station according to user location
        id_list = [x[1] for x in distid_list]
        name_cleaned = []
        city_cleaned = []
        suburb_cleaned = []
        owner_cleaned = []
        lngs_cleaned = []
        lats_cleaned = []
        ports_cleaned = []
        dc_cleaned = []
        ac_cleaned = []
        price_cleaned = []
        restroom_cleaned = []
        cctv_cleaned = []
        closing_cleaned = []
        opening_cleaned = []
        for cs in cslist:
            name_cleaned.append(str(cs.name))
            city_cleaned.append(str(cs.city))
            suburb_cleaned.append(str(cs.suburb))
            owner_cleaned.append(str(cs.owner.user.username))
            lats_cleaned.append(float(cs.lat))     
            lngs_cleaned.append(float(cs.lng))  
            ports_cleaned.append(int(cs.no_of_ports))
            dc_cleaned.append(int(cs.fast_dc))
            ac_cleaned.append(int(cs.slow_ac))
            price_cleaned.append(float(cs.price_kwh))
            restroom_cleaned.append(int(cs.restroom))
            cctv_cleaned.append(int(cs.cctv))
            opening_cleaned.append(str(cs.opening_time))
            closing_cleaned.append(str(cs.closing_time))
        csdata = [list(x) for x in zip(
            name_cleaned , city_cleaned , suburb_cleaned, owner_cleaned, 
            lats_cleaned, lngs_cleaned, ports_cleaned, dc_cleaned, 
            ac_cleaned, price_cleaned, restroom_cleaned, cctv_cleaned, 
            opening_cleaned, closing_cleaned )]
        # Get all objects according to id   
        # print(id_list)
        # to preserve order SO!
        preserved = Case(*[When(pk=pk, then=pos) for pos, pk in enumerate(id_list)])
        cslist = ChargingStation.objects.filter(pk__in = id_list).order_by(preserved)

        print(cslist)
        context = {
            'csdata': json.dumps(csdata),
            'cslist' : cslist
        }
        return render(request,'userapp/consumer_charging_stations.html', context = context)
    return redirect('index')

@login_required
def ChargingStationAnalytics(request,pk):
    if request.user.is_provider:
        current_cs = ChargingStation.objects.get(id=pk)
        # how many consumers visited this charging station
        reportcount = ChargingStationRecord.objects.filter(cs=current_cs).count()
        # total charging station of the provider
        cscount = ChargingStation.objects.filter(owner=request.user.provider).count()
        # find one sample csreport of current charging station
        report = CsReport.objects.filter(cs=current_cs)[0]
        allrecords = ChargingStationRecord.objects.filter(cs=current_cs)
        freq = []
        for i in range(24):
            # getattr to access changing field anme
            freq.append(getattr(report,'t'+str(i)))
        wholecs = ChargingStationRecord.objects.all()
        consumption = []
        sum = 0
        n = 0
        for ele in wholecs:
            n+=1
            sum+=ele.elec_consumption
        sum/=n
        consumption.append(sum)
        csrecord = ChargingStationRecord.objects.filter(cs=current_cs)
        sum = 0
        n = 0
        for cs in csrecord:
            n+=1
            sum=sum + cs.elec_consumption
        consumption.append(sum)
        weekreport = ChargingStationWeekly.objects.filter(cs=current_cs)[0]
        wr = []
        for i in range(7):
            wr.append(getattr(weekreport,'d'+str(i+1)))
        context = {
            'totalcount':reportcount,
            'cscount': cscount,
            'freq': json.dumps(freq),
            'consumption':json.dumps(consumption),
            'wr':json.dumps(wr)
        }
        return render(request,"userapp/analytics_v2.html",context=context)
    return redirect('index')

@login_required
def ChargingStationDashboard(request,pk):
    if request.user.is_provider:
        current_cs = ChargingStation.objects.get(id=pk)
        # get all records of the current_cs
        allrecords = ChargingStationRecord.objects.filter(cs=current_cs)
        username_cleaned = []
        vehicle_cleaned = []
        duration_cleaned = []
        consumption_cleaned = []
        for record in allrecords:
            username_cleaned.append(str(record.consumer.user.username))
            vehicle_cleaned.append(str(record.vehicle.company))
            duration_cleaned.append(int(record.duration))
            consumption_cleaned.append(int(record.elec_consumption))
        recorddata = [list(x) for x in zip(username_cleaned,
            vehicle_cleaned, duration_cleaned, consumption_cleaned)]
        print(recorddata)
        context = {
            'records':recorddata
        }
        return render(request,"userapp/dashboard.html",context=context)
    return redirect('index')

# def vehicledata_c(request):
@login_required
def ChargePooling(request):
    if request.user.is_consumer:
        chargepoolers = ChargePooler.objects.all()
        context = {
            'chargepoolers' : chargepoolers
        }
        return render(request,"userapp/chargepoolerpage.html",context = context)
    return redirect('index')
# def vehicledata_c(request):
#     return render(request, "userapp/vehicledata_c.html")
# def vehicledata_p(request):
#     return render(request, "userapp/vehicledata_p.html")

@login_required
def RouteYourWay(request):
    if request.user.is_consumer:
        cslist = ChargingStation.objects.all()
        # Sorted id of Charging Station according to user location
        name_cleaned = []
        city_cleaned = []
        suburb_cleaned = []
        owner_cleaned = []
        lngs_cleaned = []
        lats_cleaned = []
        ports_cleaned = []
        dc_cleaned = []
        ac_cleaned = []
        price_cleaned = []
        restroom_cleaned = []
        cctv_cleaned = []
        closing_cleaned = []
        opening_cleaned = []
        for cs in cslist:
            name_cleaned.append(str(cs.name))
            city_cleaned.append(str(cs.city))
            suburb_cleaned.append(str(cs.suburb))
            owner_cleaned.append(str(cs.owner.user.username))
            lats_cleaned.append(float(cs.lat))     
            lngs_cleaned.append(float(cs.lng))  
            ports_cleaned.append(int(cs.no_of_ports))
            dc_cleaned.append(int(cs.fast_dc))
            ac_cleaned.append(int(cs.slow_ac))
            price_cleaned.append(float(cs.price_kwh))
            restroom_cleaned.append(int(cs.restroom))
            cctv_cleaned.append(int(cs.cctv))
            opening_cleaned.append(str(cs.opening_time))
            closing_cleaned.append(str(cs.closing_time))
        csdata = [list(x) for x in zip(
            name_cleaned , city_cleaned , suburb_cleaned, owner_cleaned, 
            lats_cleaned, lngs_cleaned, ports_cleaned, dc_cleaned, 
            ac_cleaned, price_cleaned, restroom_cleaned, cctv_cleaned, 
            opening_cleaned, closing_cleaned )]
        context = {
            'csdata': json.dumps(csdata),
        }
        return render(request,"userapp/routeyourway.html",context=context)
    return redirect('index')
def temp(request):
    return render(request,"userapp/dashboard.html")

class MaintenanceMan(CreateView):
    model = MaintenanceManDetails
    template_name='MaintenanceManForm.html'
    fields = ['name','OrgName','ph1','ph2','OfficeAdd','City','AreaLocality']
    def form_valid(self, form):
        form.instance.own=self.request.user.provider
        return super().form_valid(form)

@login_required
def bookMaintenanceMan(request,pk):
    cscount = ChargingStation.objects.filter(owner=request.user.provider)
    if request.user.is_provider:

        if request.method == 'POST':

            if request.POST.get('problem'):
                CsM=CsMaintenance()
                # get the id from url for maintenanca
                # get reueds .user.
                # get descrip
                CsM.csm = request.user.provider
                CsM.Mm_id=pk
                CsM.Problem = request.POST.get('problem')
                CsM.ph =request.POST.get('phone')
                cname= request.POST.get('Cs')
                c = ChargingStation.objects.filter(name=cname)[0]
                CsM.CsSelect = c
                CsM.save()
        return render(request,"booking.html",{'cs':cscount})

class SearchListView(ListView):
    model = MaintenanceManDetails
    template_name='userapp/table.html'
    context_object_name='d'

def MaintenanceDashboard(request):
    if request.user.is_provider:

        return render(request,"userapp/maintenance_dashboard.html")

class ComplaintsListView(ListView):
    model = CsMaintenance
    template_name='userapp/complaint_dashboard.html'
    context_object_name='d'
    # def get_queryset(self):
    #     return CsMaintenance.objects.filter(Mm_own=self.request.user.provider)

def MaintenanceComplaint(request):
    # current_proviider = Provider.objects.get(user)
    m = MaintenanceManDetails.objects.get(own=request.user.provider)
    d = m.jobs.all()
    count = m.jobs.count()
    if request.method == 'POST':
        visited=request.POST.get('visited')
        CsMaintenance.objects.get(pk=visited).delete()
        m.CompletedComplaints=m.CompletedComplaints+1
    total=count+m.CompletedComplaints
    return render(request,"userapp/complaint_dashboard.html",{'d':d,'count':count,'m':m,'total':total})
    
def PendingComplaintsListView(request):
    return render(request,"userapp/complaint_dashboard.html")

def test23(request):
    return (request,"analytics_v2.html",{})