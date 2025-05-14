from rest_framework import serializers
from .models import Order, OrderItem
from meals.models import Meals

class OrderItemSerializer(serializers.ModelSerializer):
    meal_name = serializers.CharField(source='meal.meal_name')
    price = serializers.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        model = OrderItem
        fields = ['meal_name', 'quantity', 'price']


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)
    total_price = serializers.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        model = Order
        fields = ['order_id', 'user', 'restaurant', 'items', 'total_price', 'address', 'created_at', 'updated_at']
        read_only_fields = ['user', 'created_at', 'updated_at']

