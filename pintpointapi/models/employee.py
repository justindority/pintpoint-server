from django.db import models
from django.contrib.auth.models import User
from datetime import date
import django
import django.utils.timezone

class Employee(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    hourly_rate = models.DecimalField(max_digits=5, decimal_places=2)
    hire_date = models.DateField(null=False)
    term_date = models.DateField(null=True, default=None)