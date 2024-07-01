from django.db import models

# Create your models here.


class Employee(models.Model):

    empname=models.CharField(max_length=200)

    designation=models.CharField(max_length=200)

    salary=models.PositiveIntegerField()

    location=models.CharField(max_length=200)

    email=models.CharField(max_length=200)

    address=models.CharField(max_length=200)


    def __str__(self):

        return self.empname