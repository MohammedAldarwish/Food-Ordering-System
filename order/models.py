from django.db import models
from django.contrib.auth import get_user_model
from restaurant.models import Restaurant
from meals.models import Meals
import uuid



User = get_user_model()
class Order(models.Model):
    order_id = models.CharField(max_length=36, unique=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    address = models.TextField()
    total_price = models.DecimalField(max_digits=8, decimal_places=2)
    total_price = models.DecimalField(max_digits=8, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Order {self.order_id} for {self.user}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items' ,on_delete=models.CASCADE)
    meal = models.ForeignKey(Meals, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.quantity} of {self.meal.meal_name} in order {self.order.order_id}"
