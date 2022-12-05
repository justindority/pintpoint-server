from django.db import models

class Tab(models.Model):

    employee: models.ForeignKey("Employee")
    customer: models.ForeignKey("Customer", blank=True)
    gratuity: models.DecimalField(blank=True)
    closed: models.BooleanField(default=False)
    items: models.ManyToManyField("Item")