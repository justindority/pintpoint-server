from django.db import models

class Item(models.Model):

    name: models.CharField(max_length=100)
    maker: models.CharField(max_length=100)
    price: models.DecimalField(decimal_places=2)
    type: models.ForeignKey("ItemType", on_delete=models.CASCADE)
    active: models.BooleanField(default=True)    