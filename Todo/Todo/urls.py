"""
URL configuration for Todo project.

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

from taskapp import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('taskapp/add/',views.TaskCreateView.as_view(),name="task-add"),

    path('taskapp/detail/',views.TaskDetailView.as_view(),name="task-detail"),

    path('taskapp/edit/',views.TaskUpdateView.as_view(),name="task-edit"),

    path('taskapp/remove/',views.TaskDeleteView.as_view(),name="task-delete"),

    path('taskapp/summery',views.TaskSummeryView.as_view(),name="task-summery"),

    path('register/',views.SignUpView.as_view(),name='register'),

    path('',views.SignInView.as_view(),name='signin'),

    path('signout/',views.SignOutView.as_view(),name='signout')

]
