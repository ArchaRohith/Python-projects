"""
URL configuration for Employee project.

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

from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('employee/all/',views.EmployeeListView.as_view(),name="employee-list"),

    path('employee/add/',views.EmployeeAddView.as_view(),name="emp-add"),

    path('employee/<int:pk>/',views.EmployeeDetailedView.as_view(),name="emp-detail"),

    path('employee/<int:pk>/remove/',views.EmployeeDeleteView.as_view(),name="emp-delete"),

    path('employee/<int:pk>/change/',views.EmployeeEditView.as_view(),name="emp-edit"),
]
