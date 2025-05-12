from rest_framework import serializers
from .models import CartItem, Cart

class CartItemSerializers(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ['id', 'meal', 'quantity']

    def validate_quantity(self, value):
        if value < 0:
            raise serializers.ValidationError("Quantity must be greater than zero.")
        return value
    
class CartSerializers(serializers.ModelSerializer):
    items = CartItemSerializers(many=True, read_only=True)
    total_price = serializers.SerializerMethodField()

    class Meta:
        model = Cart
        fields = ['id', 'user', 'items', 'created_at', 'total_price']
        read_only_fields = ['user', 'created_at']

    def get_total_price(self, obj):
        total = 0
        for item in obj.items.all():
            total = item.total_price
        return total