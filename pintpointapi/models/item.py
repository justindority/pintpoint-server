from django.db import models

class Item(models.Model):

    name: models.CharField(max_length=100)
    price: models.DecimalField(decimal_places=2)
    type: models.ForeignKey("ItemType")