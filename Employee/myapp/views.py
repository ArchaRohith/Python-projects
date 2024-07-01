from django.shortcuts import render,redirect

# Create your views here.
from django.views.generic import View

from myapp.models import Employee

from myapp.forms import EmployeeForm

class EmployeeListView(View):

    def get(self,request,*args,**kwargs):

        qs=Employee.objects.all()

        return render(request,"employee_list.html",{"data":qs})
    

class EmployeeAddView(View):

    def get(self,request,*args,**kwargs):

        
        form_instance=EmployeeForm()

        return render(request,"emp_add.html",{"form":form_instance})
    
    def post(self,request,*args,**kwargs):

        form_instance=EmployeeForm(request.POST)

        if form_instance.is_valid():

            data=form_instance.cleaned_data

            Employee.objects.create(**data)

            return redirect("employee-list")
        
        else:

            return render(request,"emp-add.html",{"form":form_instance})


        

class EmployeeDetailedView(View):

    def get (self,request,*args,**kwargs):

        id=kwargs.get("pk")

        qs=Employee.objects.get(id=id)

        return render(request,"emp_detail.html",{"data":qs})
    

class EmployeeDeleteView(View):

    def get(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        Employee.objects.get(id=id).delete()

        return redirect("employee-list")
    
class EmployeeEditView(View):

    def get(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        movie_object=Employee.objects.get(id=id)

        dictionary={

            "empname":movie_object.empname,
            "designation":movie_object.designation,
            "salary":movie_object.salary,
            "location":movie_object.location,
            "email":movie_object.email,
            "address":movie_object.address            
        }

        form_instance=EmployeeForm(initial=dictionary)

        return render(request,"emp_edit.html",{"form":form_instance})
    

    def post(self,request,*args,**kwargs):

        form_instance=EmployeeForm(request.POST)

        id=kwargs.get("pk")

        if form_instance.is_valid():

            data=form_instance.cleaned_data

            Employee.objects.filter(id=id).update(**data)

            return redirect("employee-list")
        
        else:

            return render(request,"emp_edit.html",{"form":form_instance})