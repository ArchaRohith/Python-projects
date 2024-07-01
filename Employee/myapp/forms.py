from django import forms

class EmployeeForm(forms.Form):

    empname=forms.CharField()

    designation=forms.CharField()

    salary=forms.IntegerField()

    location=forms.CharField()

    email=forms.CharField()

    address=forms.CharField()
