from django.db import models
from django.contrib.auth.models import User

class Employee(models.Model):

    user: models.OneToOneField(User, on_delete=models.CASCADE)
    hourly_rate: models.DecimalField(decimal_places=2)
    hire_date: models.DateField
    term_date: models.DateField(blank=True)