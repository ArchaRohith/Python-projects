"""
URL configuration for calculator project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from operations.views import AdditionView,SubtactionView,MultiplicationView,FactorialView,PrimeNumberView,BmiView,SignUpView,BmrView,EmiCalculatorView,TempConversionView,BmrversionTwoView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('add/',AdditionView.as_view()),
    path('subtract/',SubtactionView.as_view()),
    path('multiplication/',MultiplicationView.as_view()),
    path('factorial/',FactorialView.as_view()),
    path('prime/',PrimeNumberView.as_view()),
    path('bmi/',BmiView.as_view()),
    path('register/',SignUpView.as_view()),
    path('bmr/',BmrView.as_view()),
    path('emi/',EmiCalculatorView.as_view()),
    path('temp/',TempConversionView.as_view()),
    path('bmr/v2/',BmrversionTwoView.as_view()),
]
