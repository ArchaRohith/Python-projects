from django.shortcuts import render

# Create your views here.
from django.views.generic import View

class GoodMorningView(View):

    def get(self,request,*args,**kwargs):
        return render(request, "morning.html")
    

class HelloWorldView(View):

    def get(self,request,*args,**kwargs):
        return render(request,"helloworld.html")
    

  
class GoodAfternoonView(View):

    def get(self,request,*args,**kwargs):
        return render(request, "afternoon.html")
   
  
class GoodEveningView(View):

    def get(self,request,*args,**kwargs):
        return render(request, "goodevening.html")
    

  
class GoodNightView(View):

    def get(self,request,*args,**kwargs):
        return render(request, "goodnight.html")
   
   
class SelfIntroView(View):


    def get(self,request,*args,**kwargs):
        return render(request,"intro.html")
    



class BatchInfoView(View):

    def get(self,request,*args,**kWargs):

        data={
            "batch_name":"python november",
            "students_count":45,
            "faculty":"sajay"
            }
        return render(request,"batchinfo.html",data)


class CourseInfoView(View):

    def get(self,request,*args,**kwargs):

        data={"name":"Django","duration":"7months"}
     

        return render(request,"info.html",data)




class PersonInfoView(View):
    def get(self,request,*args,**kqargs):

        data={"name":"sachin","game":"cricket","no_of_tournament":150},
        
        return render(request,"sachin.html",data)
        
    


# class PersonInfoView(View):
#     def get(self,request,*args,**kqargs):
         

#         data={"name":"dhoni","game":"cricket","no_of_tournament":100}

#         return render(request,"dhoni.html",data)
    