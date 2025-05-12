from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()

class Restaurant(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    restaurant_name = models.CharField(max_length=200)
    restaurant_phone = models.CharField(max_length=40, unique=True)
    restaurant_location = models.CharField(max_length=200)
    is_approved = models.BooleanField(default=False)
    open_time = models.CharField(max_length=20)  
    close_time = models.CharField(max_length=20)  
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.restaurant_name


class RestaurantImage(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='restaurant_images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
