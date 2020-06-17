from rest_framework import serializers

from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    id = serializers.CharField(source='product_id')
    class Meta:
        model = Product
        fields = (
            'id',
            'name',
            'value',
            'discount',
            'stock',
        )
