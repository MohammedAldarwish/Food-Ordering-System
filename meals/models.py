from django.db import models
from restaurant.models import Restaurant
from django.contrib.auth import get_user_model


class Category(models.Model):
    category_name = models.CharField(max_length=120)

    def __str__(self):
        return self.category_name


User = get_user_model()

class Meals(models.Model):
    added_by = models.ForeignKey(User, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='meals')
    meal_name = models.CharField(max_length=220)
    meal_description = models.TextField()
    meal_price = models.DecimalField(max_digits=6, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='meals')
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self): 
        return self.meal_name
    
class MealsImages(models.Model):
    meal = models.ForeignKey(Meals, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='meals_images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"image for {self.meal.meal_name}"

class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    meal = models.ForeignKey(Meals, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'meal')

    