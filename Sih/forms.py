from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from userapp.models import Consumer,Provider,User

class UserSignUpForm(UserCreationForm):
    class Meta():
        fields = ['username','email','password1','password2']
        model = User

class ConsumerFieldForm(forms.ModelForm):
    class Meta():
        fields = ['have_vehicle','city']
        model = Consumer
        labels ={
            'have_vehicle' : 'Do you Have an EV?'
        }

class ProviderFieldForm(forms.ModelForm):
    class Meta():
        fields = ['business_name']
        model = Provider
        labels = {
            'business_name' : 'Business Name'
        }

