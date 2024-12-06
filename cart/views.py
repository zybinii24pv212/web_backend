from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from cart.models import Cart, CartItem
from cart.serializers import CartSerializer
from product.models import ProductModel


class CartViewSet(viewsets.ModelViewSet):
    serializer_class = CartSerializer
    queryset = Cart.objects.all()
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @action(detail=False, methods=['get'])
    def get_cart(self, request):
        cart, created = Cart.objects.get_or_create(user=request.user)
        serializer = self.get_serializer(cart)
        return Response(serializer.data)

    @action(detail=False, methods=['post'])
    def add_item(self, request):
        """Добавить товар в корзину"""
        cart, created = Cart.objects.get_or_create(user=request.user)
        product_id = request.data.get('product_id')
        quantity = request.data.get('quantity', 1)

        if not product_id:
            return Response({"error": "Не указан ID продукта"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            product = ProductModel.objects.get(id=product_id)
        except ProductModel.DoesNotExist:
            return Response({"error": "Продукт не найден"}, status=status.HTTP_404_NOT_FOUND)

        cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
        if not created:
            cart_item.quantity += int(quantity)
        else:
            cart_item.quantity = int(quantity)
        cart_item.save()

        return Response({"success": "Товар добавлен в корзину"}, status=status.HTTP_200_OK)

    @action(detail=False, methods=['post'])
    def remove_item(self, request):
        """Удалить товар из корзины"""
        cart, created = Cart.objects.get_or_create(user=request.user)
        product_id = request.data.get('product_id')

        if not product_id:
            return Response({"error": "Не указан ID продукта"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            cart_item = CartItem.objects.get(cart=cart, product_id=product_id)
            cart_item.delete()
        except CartItem.DoesNotExist:
            return Response({"error": "Товар не найден в корзине"}, status=status.HTTP_404_NOT_FOUND)

        return Response({"success": "Товар удален из корзины"}, status=status.HTTP_200_OK)

    @action(detail=True, methods=['post'])
    def update_item(self, request):
        """Изменить количество товара в корзине"""
        cart = self.get_object()
        product_id = request.data.get('product_id')
        quantity = request.data.get('quantity')

        if not product_id or quantity is None:
            return Response({"error": "Необходимо указать ID продукта и количество"},
                            status=status.HTTP_400_BAD_REQUEST)

        try:
            cart_item = CartItem.objects.get(cart=cart, product_id=product_id)
            cart_item.quantity = int(quantity)
            cart_item.save()
        except CartItem.DoesNotExist:
            return Response({"error": "Товар не найден в корзине"}, status=status.HTTP_404_NOT_FOUND)

        return Response({"success": "Количество товара обновлено"}, status=status.HTTP_200_OK)

    @action(detail=True, methods=['post'])
    def buy(self, request, pk=None):
        cart = self.get_object()
        cart.items.all().delete()
        return Response({"success": "Покупка завершена, корзина очищена"}, status=status.HTTP_200_OK)
