from django.db import models


class Product(models.Model):
    product_id = models.CharField(max_length=32)
    name = models.CharField(max_length=56)
    value = models.FloatField()
    discount = models.FloatField(null=True, blank=True)
    stock = models.IntegerField()
