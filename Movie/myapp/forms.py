from django import forms

class MovieForm(forms.Form):

    title=forms.CharField()

    language=forms.CharField()

    genre=forms.CharField()