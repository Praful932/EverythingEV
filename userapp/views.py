from django.shortcuts import render, redirect
from django.http import HttpResponse
from userapp.forms import UserSignUpForm, ConsumerSignUpForm
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from userapp.models import User, Consumer, Provider, Vehicle

# Create your views here.

def index(request):
    return render(request,"userapp/index.html")

def register(request):
    return render(request,"userapp/register.html")

def registerCustomer(request):
    if request.user.is_authenicated:
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
        signupform = ConsumerSignUpForm()
        consumerform = UserSignUpForm()
    context = {
        'signupform' : signupform,
        'consumerform' : consumerform
    }
    return render(request, "userapp/registerCustomer.html", context = context)






# def stations(request):
#     return render(request, "userapp/stations.html")

def stations_user(request):
    return render(request, "userapp/user_charging.html")

# def vehicledata_c(request):
#     return render(request, "userapp/vehicledata_c.html")
# def vehicledata_p(request):
#     return render(request, "userapp/vehicledata_p.html")
