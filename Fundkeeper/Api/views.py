from django.shortcuts import render

from django.utils import timezone

from rest_framework.response import Response

from rest_framework.views import APIView

from rest_framework import authentication,permissions

from rest_framework.viewsets import ModelViewSet

from Api.serializers import UserSerializer

from Api.serializers import IncomeSerializer,ExpenseSerializer

from Api.permissions import OwnerOnly

from budget.models import Income,Expense

from django.db.models import Sum

class UserCreationView(APIView):

    def post(self,request,*args,**kwargs):

        serializer_instance=UserSerializer(data=request.data)

        if serializer_instance.is_valid():

            serializer_instance.save()

            return Response(data=serializer_instance.data)
        

        else:

            return Response(data=serializer_instance.errors)
        


class IncomeViewset(ModelViewSet):

    serializer_class=IncomeSerializer

    queryset=Income.objects.all()



    authentication_classes=[authentication.TokenAuthentication]

    permission_classes=[OwnerOnly]

    def list(self,request,*args,**kwargs):

        qs=Income.objects.filter(user_object=request.user)

        serailizer_instance=IncomeSerializer(qs,many=True)

        return Response(data=serailizer_instance.data)


    def perform_create(self, serializer):

        return serializer.save(user_object=self.request.user)
    



class IncomesummeryView(APIView):

    permission_classes=[permissions.IsAuthenticated]

    #  authentication_classes=[authentication.BasicAuthentication]

    authentication_classes=[authentication.TokenAuthentication]

    def get(self,request,*args,**kwargs):

        current_month=timezone.now().month

        current_year=timezone.now().year
        
        all_incomes=Income.objects.filter(

            user_object=request.user,

            created_date__month=current_month,

            created_date__year=current_year
        )

        income_total=all_incomes.values("amount").aggregate(total=Sum("amount"))

        category_summery=all_incomes.values("category").annotate(totals=Sum("amount"))

        data={

            "income_total":income_total,

            "category_summery":category_summery

        }

        return Response(data=data)




class ExpenseViewset(ModelViewSet):

    serializer_class=ExpenseSerializer

    queryset=Expense.objects.all()

    # authentication_classes=[authentication.BasicAuthentication]

    authentication_classes=[authentication.TokenAuthentication]

    permission_classes=[permissions.IsAuthenticated]

    

    permission_classes=[OwnerOnly]

    def list(self,request,*args,**kwargs):

        qs=Expense.objects.filter(user_object=request.user)

        serailizer_instance=ExpenseSerializer(qs,many=True)

        return Response(data=serailizer_instance.data)


    def perform_create(self, serializer):

        return serializer.save(user_object=self.request.user)
    



class ExpensesummeryView(APIView):

    permission_classes=[permissions.IsAuthenticated]

    # authentication_classes=[authentication.BasicAuthentication]

    authentication_classes=[authentication.TokenAuthentication]

    def get(self,request,*args,**kwargs):

        current_month=timezone.now().month

        current_year=timezone.now().year
        
        all_expenses=Expense.objects.filter(

            user_object=request.user,

            created_date__month=current_month,

            created_date__year=current_year
        )

        expense_total=all_expenses.values("amount").aggregate(total=Sum("amount"))

        category_summery=all_expenses.values("category").annotate(totals=Sum("amount"))

        priority_summery=all_expenses.values("priority").annotate(total=Sum("amount"))

        data={

            "expense_total":expense_total,

            "category_summery":category_summery,

            "priority_summery":priority_summery
        }

        return Response(data=data)

