from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from userapp.models import Consumer, Provider, User, Vehicle

class UserSignUpForm(UserCreationForm):
    class Meta():
        fields = ['username','email','password1','password2']
        model = User

class ConsumerSignUpForm(forms.ModelForm):
    class Meta():
        fields = ['have_vehicle','city']
        model = Consumer
        labels = {
            'have_vehicle': 'Do you have an EV?',
            'city': 'City'
        }

class ProviderSignUpForm(forms.ModelForm):
    class Meta():
        fields = ['business_name']
        model = Provider
        labels = {
            'business_name': 'Business Name'
        }

class UserUpdateForm(forms.ModelForm):
    class Meta():
        fields = ['username','email']
        model = User

class ChargingStationForm(forms.ModelForm):
    class Meta():
        fields = ['lat','lng','no_of_ports',
        'fast_dc','slow_ac','price_kwh','restroom','cctv','opening_time','closing_time','image']
        labels = {
            'no_of_ports':'No of Ports',
            'fast_dc' : 'Fast Ports',
            'slow_ac' : 'Slow ports'
        }