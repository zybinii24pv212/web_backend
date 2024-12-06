from django.shortcuts import render
from rest_framework import viewsets

from product.models import ProductModel
from product.serializers import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = ProductModel.objects.all()
