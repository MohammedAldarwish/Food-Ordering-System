from rest_framework import serializers
from .models import Meals, MealsImages, Category, Favorite

class MealsImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = MealsImages
        fields = ['id', 'image']

<<<<<<< HEAD

class MealSerializer(serializers.ModelSerializer):
    images = MealsImageSerializer(many=True, read_only=True)
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())

    # Exclude 'restaurant' from input and make it read-only
    class Meta:
        model = Meals
        fields = ['meal_name', 'meal_description', 'meal_price', 'images', 'category']  # No 'restaurant' here
        read_only_fields = ['restaurant']  # Mark 'restaurant' as read-only

        
=======
class MealSerializer(serializers.ModelSerializer):
    images = MealsImageSerializer(many=True, read_only=True)
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
    class Meta:
        model = Meals
        fields = ['restaurant', 'meal_name', 'meal_description', 'meal_price' ,'images', 'category']
         

>>>>>>> 384d072cae553316b277c547a712ba2176ce2416
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