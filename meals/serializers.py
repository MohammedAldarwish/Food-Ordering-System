from rest_framework import serializers
from .models import Meals, MealsImages, Category, Favorite

class MealsImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = MealsImages
        fields = ['id', 'image']

class MealSerializer(serializers.ModelSerializer):
    images = MealsImageSerializer(many=True, read_only=True)
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
    class Meta:
        model = Meals
        fields = ['restaurant', 'meal_name', 'meal_description', 'meal_price' ,'images', 'category']
         

class FavoriteSerializer(serializers.ModelSerializer):
    meal_id = serializers.PrimaryKeyRelatedField(
        queryset=Meals.objects.all(),
        source='meal',
        write_only=True
    )
    meal = MealSerializer(read_only=True)

    class Meta:
        model = Favorite
        fields = ['id', 'meal', 'meal_id']

    def validate_meal(self, value):
        if not value:
            raise serializers.ValidationError('Meal cannot be null.')
        return value