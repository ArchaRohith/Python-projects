from django.shortcuts import render

# Create your views here.

from django.views.generic import View

class AdditionView(View):


    def get(self,request,*args,**kwargs):

        return render(request,"add.html")


    def post(self,request,*args,**kwargs):
        num1=request.POST.get("box1")
        num2=request.POST.get("box2")
        result=int(num1)+int(num2)
        print(result)
        return render(request,"add.html")
    



class SubtactionView(View):

    def get(self,request,*args,**kwargs):

        return render(request,"subtract.html")
    
    def post(self,request,*args,**kwargs):

        num1=request.POST.get("box1")
        num2=request.POST.get("box2")
        result=int(num1)-int(num2)
        print(result)
        return render(request,"subtract.html")




class MultiplicationView(View):

    def get(self,request,*args,**kwargs):

        return render(request,"multiplication.html")
    
    def post(self,request,*args,**kwargs):
        num1=request.POST.get("box1")
        num2=request.POST.get("box2")
        result=int(num1)*int(num2)
        print(result)
        return render(request,"multiplication.html",{"data":result})
    


class FactorialView(View):

    def get(self,request,*args,**kwargs):

        return render(request,"factorial.html")
    
    def post(self,request,*args,**kwargs):

        num=int(request.POST.get("box"))
        result=1
        for i in range(1,(num+1)):
            result=result*i
        return render(request,"factorial.html",{"data":result})
    


class PrimeNumberView(View):

    def get(self,request,*args,**kwargs):

        return render(request,"prime.html")
    
    def post(self,request,*args,**kwargs):

        num=int(request.POST.get("box"))

        is_prime=True
        for i in range(2,num):
            if num%i==0:
                is_prime=False
                break
        return render(request,"prime.html",{"data":is_prime})
    




class BmiView(View):

    def get(self,request,*args,**kwargs):

        return render(request,"bmi.html")
    

    def post(self,request,*args,**kwargs):

        height=int(request.POST.get("hbox"))
        weight=int(request.POST.get("wbox"))
        height_in_meter=height/100
        bmi=weight/(height_in_meter)**2
        bmi=round(bmi,2)


        result=""
        if bmi<19:
            result="underweight"
        elif bmi<25:
            result="normal weight"
        
        elif bmi <30:
            result="over weight"

        elif bmi >30:
            result="obese"
            

        return render(request,"bmi.html",{"data":result})
    






from operations.forms import RegistrationForm

class SignUpView(View):

    def get(self,request,*args,**kwargs):

        form=RegistrationForm()

        return render(request,"register.html",{"form":form})




from operations.forms import BmrForm


class BmrView(View):
   
    def get(self,request,*args,**kwargs):
       
       form=BmrForm() #create instance /object of bmrform

       return render(request,"bmr.html",{"form":form})


    def post(self,request,*args,**kwargs):
       
       height=int(request.POST.get("height"))


       weight=int(request.POST.get("weight"))


       age=int(request.POST.get("age"))


       gender=request.POST.get("gender")

       activity_level=int(request.POST.get("activity_level"))


       print(height,weight,age,gender,activity_level)

       bmr=0
       
       if gender=="male":
           
           bmr=(10*weight)+(6.25*height)-(5*age)+5

       elif gender=="female":
           
           bmr=(10*weight)+(6.25*height)-(5*age)-161


       form=BmrForm()

       calorie=0

       if activity_level==1:
           
           calorie=bmr*1.2

       elif activity_level==2:
           
           calorie=bmr*1.375

       elif activity_level==3:
           
           calorie=bmr*1.55

       elif activity_level==4:
           
           calorie=bmr*1.725

       elif activity_level==5:
           
           calorie=bmr*1.9


       print(bmr)


       print(f"number of calories you need in ordere to maintain your current weight={calorie}")


       return render(request,"bmr.html",{"form":form})
    
       

class BmrversionTwoView(View):

    def get(self,request,*args,**kwargs):
       
       form_instance=BmrForm()

       return render(request,"bmrsecond.html",{"form":form_instance})
    
    def post(self,request,*args,**kwargs):

        form_instance=BmrForm(request.POST)

        if form_instance.is_valid():

            # print(form_instance.cleaned_data)

            validated_data=form_instance.cleaned_data

            height=validated_data.get("height")

            weight=validated_data.get("weight")

            age=validated_data.get("age")

            gender=validated_data.get("gender")

            activity_level=validated_data.get("activity_level")

            print(height,weight,age,gender,activity_level)


            bmr=0

            if gender=="male":

                bmr=(10*weight)+(6.25*height)-(5*age)+5

            elif gender=="female":

                bmr=(10*weight)+(6.25*height)-(5*age)-161
            
            print(bmr)

            activity_level_values={"1":1.2,"2":1.375,"3":1.55,"4":1.725,"5":1.9}

            calorie=bmr*activity_level_values.get(activity_level)

            print(calorie)

            context={"data":calorie}


            return render(request,"bmrsecond.html",{"form":form_instance,"data":calorie})

            
        
        else:

            print("error")

            return render(request,"bmrsecond.html",{"form":form_instance})













from operations.forms import EmiForm

class EmiCalculatorView(View):

    def get(self,request,*args,**kwargs):

        form=EmiForm()

        return render(request,"emi.html",{"form":form})
    
    def post(self,request,*args,**kwargs):

        amount=request.POST.get("amount")

        interest=request.POST.get("interest")

        tenure=request.POST.get("tenure")

        print(amount,interest,tenure)

        form=EmiForm()

        return render(request,"emi.html",{"form":form})






from operations.forms import TemparatureForm

class TempConversionView(View):

    def get(self,request,*args,**kwargs):

        form=TemparatureForm()

        return render(request,"temp.html",{"form":form})
    

    def post(self,request,*args,**kwargs):


        form_instance=TemparatureForm(request.POST)

        if form_instance.is_valid():

            print("form has no errors")

        else:

            print("form has errors")

        return render(request,"temp.html")