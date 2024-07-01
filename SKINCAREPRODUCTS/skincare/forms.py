
from django import forms

from django.contrib.auth.models import User #user modelil save cheyyan user import cheyyanam

from django.contrib.auth.forms import UserCreationForm

class SignUpForm(UserCreationForm):

    class Meta:

        model=User

        fields=["username","email","password1","password2"]


class SignInForm(forms.Form):  #db il save and update cheyyan ellathathu kondu formilottu thanne inherit cheyyum

    username=forms.CharField()

    password=forms.CharField()

