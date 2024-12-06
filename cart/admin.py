from django.contrib import admin

from cart.models import CartItem, Cart


class CartItemInline(admin.TabularInline):
    model = CartItem
    extra = 1


class CartAdmin(admin.ModelAdmin):
    list_display = ('user',)
    inlines = [CartItemInline]


admin.site.register(Cart, CartAdmin)