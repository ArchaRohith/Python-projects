from django import forms

class StudentForm(forms.Form):

    studentname=forms.CharField()

    coursename=forms.CharField()

    fees=forms.NumberInput()