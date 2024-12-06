from django.db import models


class ProductModel(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    old_price = models.FloatField()
    description = models.TextField()
