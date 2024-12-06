from django.contrib import admin
from .models import ProductModel, ProductImage


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'old_price', 'description', 'characteristics')
    inlines = [ProductImageInline]


admin.site.register(ProductModel, ProductAdmin)



