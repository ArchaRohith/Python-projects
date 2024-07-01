from django import forms

from myapp.models import Movie

class MovieForm(forms.Form):

    title=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control border border-info"}))

    year=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control border border-info"}))

    director=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control border border-info"}))

    run_time=forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control border border-info"}))

    languages=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control border border-info"}))

    genre=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control border border-info"}))

    producer=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control border border-info"}))
    

class MovieModelForm(forms.ModelForm):

    class Meta:

        model=Movie

        #  fields=["title","year","director","run_time","languages","genre","producer"]

        exclude=("id",)

        widget={
            "title":forms.TextInput(attrs={"class":"form-control"}),

            "year":forms.TextInput(attrs={"class":"form-control"}),

            "director":forms.TextInput(attrs={"class":"form_control"}),

            "run_time":forms.TextInput(attrs={"class":"form_control"}),

            "languages":forms.TextInput(attrs={"class":"form_control"}),

            "genre":forms.TextInput(attrs={"class":"form_control"}),

            "producer":forms.TextInput(attrs={"class":"form_control"})

        }