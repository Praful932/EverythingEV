from django import forms
from django.contrib.auth.forms import UserCreationForm
from userapp.models import (Consumer, Provider, User, ChargingStation,
                            Support, UserRecord, ChargePooler)


class UserSignUpForm(UserCreationForm):
    class Meta():
        fields = ['username', 'email', 'password1', 'password2']
        model = User


class ConsumerSignUpForm(forms.ModelForm):
    class Meta():
        fields = ['have_vehicle', 'city']
        model = Consumer
        labels = {
            'have_vehicle': 'Do you have an EV?',
            'city': 'City'
        }


class ProviderSignUpForm(forms.ModelForm):
    class Meta():
        fields = ['business_name', 'image']
        model = Provider
        labels = {
            'business_name': 'Business Name',
            'image': 'Logo'
        }


class UserUpdateForm(forms.ModelForm):
    class Meta():
        fields = ['username', 'email']
        model = User


class ChargingStationForm(forms.ModelForm):
    opening_time = widget = forms.TimeInput(format='%H:%M')
    closing_time = widget = forms.TimeInput(format='%H:%M')

    class Meta():
        fields = ['name', 'lat', 'lng', 'no_of_ports',
                  'fast_dc', 'slow_ac', 'price_kwh', 'restroom', 'cctv', 'opening_time', 'closing_time', 'image']
        model = ChargingStation
        labels = {
            'name': 'Name',
            'no_of_ports': 'No of Ports',
            'fast_dc': 'Fast Ports',
            'slow_ac': 'Slow ports',
            'price_kwh': 'Price/Kwh',
            'restroom': 'Restroom',
            'opening_time': 'Opening Time',
            'closing_time': 'Closing Time',
            'image': 'Images'
        }


class SupportForm(forms.ModelForm):
    class Meta:
        model = Support
        fields = ['subject', 'description']
        labels = {
            'subject': 'Issue Title',
            'description': 'Issue Description'
        }

        widgets = {
            'description': forms.Textarea(attrs={'placeholder': 'Describe your issue here(max 200 words)'})
        }


class SurveyForm(forms.ModelForm):
    class Meta:
        model = UserRecord
        fields = ['start_time', 'stop_time', 'vehicle', 'port_type', 'lat', 'lng']


class CharpoolerForm(forms.ModelForm):
    class Meta:
        model = ChargePooler
        fields = ['city', 'local_area', 'ph_no', 'cost', 'normal_port', 'fast_port']