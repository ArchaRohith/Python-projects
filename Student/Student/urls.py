"""
URL configuration for Student project.

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

    path('student/all/',views.StudentListView.as_view(),name="student-list"),

    path('student/add/',views.StudentAddView.as_view(),name="student-add"),

    path('student/<int:pk>/',views.StudentDetailView.as_view(),name="student-detail"),

    path('student/<int:pk>/remove/',views.StudentDeleteView.as_view(),name="student-delete"),

    path('student/<int:pk>/change/',views.StudentUpdateView.as_view(),name="student-update")

]
