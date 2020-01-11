from django.shortcuts import render, redirect
from django.views.generic import DetailView, ListView, UpdateView, DeleteView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django import forms
from django.urls import reverse_lazy
from django.http import HttpResponse
from userapp.forms import UserSignUpForm, ConsumerSignUpForm, ProviderSignUpForm, UserUpdateForm, ChargingStationForm
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from userapp.models import User, Consumer, Provider, Vehicle, ChargingStation

# Create your views here.

def index(request):
    return render(request,"userapp/index.html")

def register(request):
    return render(request,"userapp/register.html")

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
            login(request,new_user)
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
    return render(request, "userapp/registerCustomer.html", context = context)

def registerProvider(request):
    if request.user.is_authenticated:
        logout(request)
    if request.method == 'POST':
        signupform = UserSignUpForm(request.POST)
        providerform = ProviderSignUpForm(request.POST)
        if signupform.is_valid() and providerform.is_valid():
            username = signupform.cleaned_data.get('username')
            new_user = signupform.save(commit = False)
            new_user.is_provider = True
            new_user = signupform.save()
            login(request,new_user)
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
        return render(request, "userapp/uc.html")
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
                stationform.save()
                return redirect('index')
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
    paginate_by = 3
    def test_func(self):
        if self.request.user.is_provider:
            return True
        return False
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_provider = Provider.objects.get(user=self.request.user)
        context['charging_stations'] = ChargingStation.objects.filter(owner=current_provider)
        return context



def foo(request):
    return render(request,"userapp/service_dashboard.html")
# def vehicledata_c(request):
#     return render(request, "userapp/vehicledata_c.html")
# def vehicledata_p(request):
#     return render(request, "userapp/vehicledata_p.html")
