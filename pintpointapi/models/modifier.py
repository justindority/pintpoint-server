from django.db import models

class Modifier(models.Model):

    modifier: models.CharField(max_length=100)
    price: models.DecimalField(decimal_places=2)