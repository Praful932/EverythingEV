from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from userapp.models import Consumer, Provider, User, Vehicle

class UserSignUpForm(UserCreationForm):
    class Meta():
        fields = ['username','email','password1','password2']
        model = User

class ConsumerSignUpForm(forms.ModelForm):
    class Meta():
        fields = ['have_vehicle','City']
        model = Consumer
        labels = {
            'have_vehicle': 'Do you have an EV?'
        }