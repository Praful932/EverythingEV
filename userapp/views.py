from django.shortcuts import render, redirect
from django.http import HttpResponse
from userapp.forms import UserSignUpForm, ConsumerSignUpForm, ProviderSignUpForm, UserUpdateForm
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from userapp.models import User, Consumer, Provider, Vehicle

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

@login_required
def ChargingStation(request):
    if request.user.is_consumer:
        return render(request, "userapp/uc.html")
    if request.user.is_provider:
        return render(request, "userapp/stations.html")
    

# def vehicledata_c(request):
#     return render(request, "userapp/vehicledata_c.html")
# def vehicledata_p(request):
#     return render(request, "userapp/vehicledata_p.html")
