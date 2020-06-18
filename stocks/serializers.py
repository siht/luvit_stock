from rest_framework import serializers

from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    id = serializers.CharField(source='product_id')
    discount_value = serializers.FloatField(source='discount', required=False)

    class Meta:
        model = Product
        fields = (
            'id',
            'name',
            'value',
            'discount_value',
            'stock',
        )
    
    def validate(self, data):
        errors = []
        if len(data['name']) < 3 or len(data['name']) > 55:
            errors.append('Invalid product name')
        if data['stock'] < 0:
            errors.append('Invalid stock value')
        if data['value'] <= 0 or data['value'] > 99999.9:
            errors.append('Invalid value')
        if data.get('discount', 0) > data['value']:
            errors.append('Invalid discount value')
        if errors:
            error_message = {
                'id': data['product_id'],
                'errors': errors
            }
            raise serializers.ValidationError(error_message)
        return data
