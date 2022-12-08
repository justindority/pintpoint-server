from django.db import models

class Item(models.Model):

    name = models.CharField(max_length=100)
    maker = models.CharField(max_length=100)
    type = models.ForeignKey("ItemType", on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    active = models.BooleanField(default=True)