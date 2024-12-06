from django.contrib import admin
from .models import ProductModel, ProductImage, CartItem, Cart


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'old_price', 'description', 'characteristics')
    inlines = [ProductImageInline]


admin.site.register(ProductModel, ProductAdmin)


class CartItemInline(admin.TabularInline):
    model = CartItem
    extra = 1


class CartAdmin(admin.ModelAdmin):
    list_display = ('user',)
    inlines = [CartItemInline]


admin.site.register(Cart, CartAdmin)
