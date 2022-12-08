from django.db import models

class Tab(models.Model):

    employee = models.ForeignKey("Employee", on_delete=models.CASCADE)
    customer = models.ForeignKey("Customer", on_delete=models.CASCADE, null=True)
    gratuity = models.DecimalField(null=True, max_digits=5, decimal_places=2)
    closed = models.BooleanField(default=False)
    items = models.ManyToManyField("Item")