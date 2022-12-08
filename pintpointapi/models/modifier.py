from django.db import models

class Modifier(models.Model):

    modifier = models.CharField(max_length=100, default="double")
    type = models.CharField(max_length=20, default="add")
    price = models.DecimalField(max_digits=4, decimal_places=2)