from django.db import models
from datetime import date
import django
import django.utils.timezone


class TabItems(models.Model):

    tab = models.ForeignKey("Tab", on_delete=models.CASCADE)
    item = models.ForeignKey("Item", on_delete=models.CASCADE)
    timestamp = models.DateField(null=False)

class Tab(models.Model):

    employee = models.ForeignKey("Employee", on_delete=models.CASCADE)
    customer = models.CharField(max_length=100)
    gratuity = models.DecimalField(null=True, max_digits=5, decimal_places=2)
    closed = models.BooleanField(default=False)
    items = models.ManyToManyField("Item", through=TabItems)

