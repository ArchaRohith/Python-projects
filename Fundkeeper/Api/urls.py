from django.urls import path

from Api import views

from rest_framework.routers import DefaultRouter

from rest_framework.authtoken.views import ObtainAuthToken

router=DefaultRouter()

router.register("incomes",views.IncomeViewset,basename="income")


router.register("expense",views.ExpenseViewset,basename="expense")

urlpatterns=[

    path('register/',views.UserCreationView.as_view()),

    path("incomes/summery/",views.IncomesummeryView.as_view()),

    path("expense/summery/",views.ExpensesummeryView.as_view()),

    path("token/",ObtainAuthToken.as_view()),

]+router.urls