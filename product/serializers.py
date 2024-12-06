from rest_framework import serializers

from product.models import ProductModel, ProductImage


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['image']


class ProductSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True, read_only=True)  # Серилизатор для изображений

    class Meta:
        model = ProductModel
        fields = '__all__'
