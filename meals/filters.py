import django_filters
from .models import Meals

class MealFilter(django_filters.FilterSet):
    category = django_filters.CharFilter(field_name='category__category_name', lookup_expr='icontains')

    class Meta:
        model = Meals
        fields = ['category', 'meal_name']