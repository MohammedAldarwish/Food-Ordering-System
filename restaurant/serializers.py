from rest_framework import serializers
from .models import Restaurant, RestaurantImage


class RestaurantImageSerializers(serializers.ModelSerializer):
    class Meta:
        model = RestaurantImage
        fields = ['id', 'image']

class RestaurantSerializers(serializers.ModelSerializer):
    images = RestaurantImageSerializers(many=True, read_only=True)
    class Meta:
        model = Restaurant
        fields = [
            'restaurant_name', 'restaurant_phone',
              'restaurant_location', 'open_time',
              'close_time', 'images'
        ]