from django import forms

from taskapp.models import TaskApp

from django.contrib.auth.models import User

class TaskAppForm(forms.Form):

    
    class Meta:

        model=TaskApp

        exclude=("id","created_date")

        widgets={

            "title":forms.TextInput(attrs={"class":"form-control"}),

            "owner":forms.TextInput(attrs={"class":"form-control"}),
            
            

        }

class RegistrationForm(forms.ModelForm):

    class Meta:

        model=User

        fields=["username","email","password"]

        widgets={

            "username":forms.TextInput(attrs={"class":"form-control"}),

            "email":forms.EmailInput(attrs={"class":"form-control"}),

            "password":forms.PasswordInput(attrs={"class":"form-control"})
        }

class LoginForm(forms.Form):

    username=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))

    password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))