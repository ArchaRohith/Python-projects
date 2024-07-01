from django.shortcuts import render,redirect

# Create your views here.

from django.views.generic import View

from myapp.models import Movie

from myapp.forms import MovieForm

class MovieListView(View):

    def get(self,request,*args,**kwargs):

        qs=Movie.objects.all()

        return render(request,"movie_list.html",{"data":qs})


class MovieAddView(View):

    def get(self,request,*args,**kwargs):

        form_instance=MovieForm()

        return render(request,"movie_add.html",{"form":form_instance})


    def post(self,request,*args,**kwargs):

        form_instance=MovieForm(request.POST)

        if form_instance.is_valid():

            data=form_instance.cleaned_data

            Movie.objects.create(**data)

            return redirect("movie-list")
        
        else:

            return render(request,"movie_add.html",{"form":form_instance})
        
        
class MovieDetailView(View):

    def get(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        qs=Movie.objects.get(id=id)

        return render(request,"movie_detail.html",{"data":qs})
    


class MovieDeleteView(View):

    def get(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        Movie.objects.get(id=id).delete()

        return redirect("movie-list")


class MovieUpdateView(View):

    def get(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        movie_object=Movie.objects.get(id=id)

        dictionary={
            "title":movie_object.title,
            "language":movie_object.language,
            "genre":movie_object.genre
        }

        form_instance=MovieForm(initial=dictionary)

        return render(request,"movie_edit.html",{"form":form_instance})
    

    def post(self,request,*args,**kwargs):

        form_instance=MovieForm(request.POST)

        id=kwargs.get("pk")

        if form_instance.is_valid():

            data=form_instance.cleaned_data      

            Movie.objects.filter(id=id).update(**data)

            return redirect("movie-list")
        
        else:

            return render(request,"movie_edit.html",{"form":form_instance})