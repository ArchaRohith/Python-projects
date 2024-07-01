from django.shortcuts import render

from rest_framework.views import APIView

from rest_framework.response import Response

from myapp.models import Movie,Actor,Album,Tracks

from api.serializers import MovieSerializer,ActorSerializer,AlbumSerializer,TrackSerializer,ReviewSerializer

from rest_framework import viewsets

from rest_framework.decorators import action

# Create your views here.

class MovieListView(APIView):

    def get(self,request,*args,**kwargs):

        qs=Movie.objects.all() #qs queryset select * from movies Quearyset

        #qs=> python native type(seralization)

        serializer_instance=MovieSerializer(qs,many=True) #onnilam athikam movie object ullath kond many=True

        return Response(data=serializer_instance.data) #Response
    
    def post(self,request,*args,**kwargs):
         
        serializer_instance=MovieSerializer(data=request.data)

        if serializer_instance.is_valid():

            serializer_instance.save()  #
         
            return Response(data=serializer_instance.data)
        
        else:

            return Response(data=serializer_instance.errors)


class MovieRetrieveUpdateDestroyView(APIView):
    
    def get(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        movie_obj=Movie.objects.get(id=id)

        seralizer_instance=MovieSerializer(movie_obj,many=False)
        
        return Response(data=seralizer_instance.data)
    

    def put(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        movie_obj=Movie.objects.get(id=id)

        seralizer_instance=MovieSerializer(data=request.data,instance=movie_obj)

        if seralizer_instance.is_valid():

            seralizer_instance.save()

            return Response(data=seralizer_instance.data)
        
        else:

            return Response(data=seralizer_instance.errors)

    def delete(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        Movie.objects.get(id=id).delete()
        
        return Response(data={"message":"deleted"})
    


class LanguagesView(APIView):

    def get(self,request,*args,**kwargs):

        qs=Movie.objects.all().values_list("languages",flat=True).distinct()

        return Response(data=qs)

class GenresView(APIView):

     def get(self,request,*args,**kwargs):

        qs=Movie.objects.all().values_list("genre",flat=True).distinct()

        return Response(data=qs)


class ActorViewSet(viewsets.ViewSet):

    def list(self,request,*args,**kwargs):

        qs=Actor.objects.all()

        serializer_instance=ActorSerializer(qs,many=True)

        return Response(data=serializer_instance.data)
    

    def create(self,request,*args,**kwargs):


        seializer_instance=ActorSerializer(data=request.data)

        if seializer_instance.is_valid():

            seializer_instance.save()

            return Response(data=seializer_instance.data)
        
        else:

            return Response(data=seializer_instance.errors)
    
    def retrieve(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        actor_obj=Actor.objects.get(id=id)

        seralizer_instance=ActorSerializer(actor_obj,many=False)

        return Response(data=seralizer_instance.data)
    
    def update(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        actor_obj=Actor.objects.get(id=id)

        seralizer_instance=ActorSerializer(data=request.data,instance=actor_obj)

        if seralizer_instance.is_valid():

            seralizer_instance.save()

            return Response(data=seralizer_instance.data)
        
        else:

            return Response(data=seralizer_instance.errors)
        

    def destroy(self,request,*args,**kwargs):
        
        id=kwargs.get("pk")

        actor_obj=Actor.objects.get(id=id).delete()


        return Response(data={"message":"delete"})



class MovieViewSet(viewsets.ModelViewSet):

    serializer_class=MovieSerializer

    queryset=Movie.objects.all()


class AlbumViewSetView(viewsets.ModelViewSet):

    serializer_class=AlbumSerializer

    queryset=Album.objects.all()


    # url localhost:8000/api/albums/languages/
    # method- get
    @action(methods=["GET"],detail=False)
    def languages(self,request,*args,**kwargs):


        qs=Album.objects.all().values_list("language",flat=True).distinct()

        return Response(data=qs)


    # url localhost:8000/api/albums/directors/
    # method =get
    @action(methods=["GET"],detail=False)
    def directors(self,request,*args,**kwargs):

        qs=Album.objects.all().values_list("director",flat=True).distinct()

        return Response(data=qs)



    # url localhost:8000/api/albums/{id}/add_track/
    # method=post

    @action(methods=["POST"],detail=True)
    def add_track(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        album_obj=Album.objects.get(id=id)

        serializer_instance=TrackSerializer(data=request.data)
        
        if serializer_instance.is_valid():
            
            serializer_instance.save(album_object=album_obj)

            return Response(data=serializer_instance.data)
        
        else:

            return Response(data=serializer_instance.errors)




    @action(methods=["POST"],detail=True)
    def add_review(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        album_obj=Album.objects.get(id=id)

        serializer_instance=ReviewSerializer(data=request.data)

        if serializer_instance.is_valid():

            serializer_instance.save(album_object=album_obj)

            return Response(data=serializer_instance.data)
        
        else:

            return Response(data=serializer_instance.errors)




class TrackViewSetView(viewsets.ModelViewSet):

    serializer_class=TrackSerializer

    queryset=Tracks.objects.all()






