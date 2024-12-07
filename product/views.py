import django_filters
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.filters import SearchFilter

from product.models import ProductModel
from product.serializers import ProductSerializer


class ProductFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = ProductModel
        fields = ['name']


class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = ProductModel.objects.all()
    filter_backends = (SearchFilter,)
    search_fields = ['name']

    def get_serializer(self, *args, **kwargs):
        """
        Return the serializer instance that should be used for validating and
        deserializing input, and for serializing output.
        """
        serializer_class = self.get_serializer_class()
        return serializer_class(*args, **kwargs)
