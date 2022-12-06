from django.db import models

class Tab(models.Model):

    employee: models.ForeignKey("Employee", on_delete=models.CASCADE)
    customer: models.ForeignKey("Customer", on_delete=models.CASCADE, blank=True)
    gratuity: models.DecimalField(blank=True)
    closed: models.BooleanField(default=False)
    items: models.ManyToManyField("Item")