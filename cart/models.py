from django.contrib.auth.models import User
from django.db import models

from product.models import ProductModel


class Cart(models.Model):
    user = models.ForeignKey(User, related_name='cart', on_delete=models.CASCADE)

    def total_price(self):
        """Метод для вычисления общей стоимости товаров в корзине"""
        total = sum(item.total_price() for item in self.items.all())
        return total


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(ProductModel, related_name='cart_items', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.product.name} - {self.quantity} шт."

    def total_price(self):
        return self.product.price * self.quantity
