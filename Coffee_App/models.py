from statistics import mode
from django.db import models
from django.shortcuts import redirect

# Create your models here.

class Appointment(models.Model):
    first_name=models.CharField(max_length=5000)
    last_name=models.CharField(max_length=5000)
    date=models.CharField(max_length=5000)
    time=models.CharField(max_length=5000)
    message=models.CharField(max_length=5000)

    def __str__(self):
        return self.first_name