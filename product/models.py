from django.contrib.auth.models import User
from django.db import models


class ProductModel(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    old_price = models.FloatField()
    description = models.TextField()
    characteristics = models.JSONField()

    def __str__(self):
        return self.name


class ProductImage(models.Model):
    product = models.ForeignKey(ProductModel, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product_images/')



