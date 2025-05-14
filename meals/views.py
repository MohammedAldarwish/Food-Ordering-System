from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from .models import Meals, Favorite
from .serializers import MealSerializer, FavoriteSerializer
from restaurant.models import Restaurant
from .filters import MealFilter
from rest_framework.exceptions import PermissionDenied
from rest_framework import serializers

class MealViewSet(viewsets.ModelViewSet):
    serializer_class = MealSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        Show meals only for the restaurant linked to the authenticated user.
        """
        return Meals.objects.filter(restaurant=self.request.user.restaurant)

    def perform_create(self, serializer):
        """
        Ensure the user has a linked restaurant before creating a meal.
        """
        try:
            restaurant = self.request.user.restaurant
        except Restaurant.DoesNotExist:
            raise serializers.ValidationError("You must have a restaurant to add meals.")
        
        # Add the current user as the added_by field
        serializer.save(restaurant=restaurant, added_by=self.request.user)

    def perform_update(self, serializer):
        """
        Allow updates only by the owner of the meal's restaurant.
        """
        meal = self.get_object()
        if meal.restaurant.user != self.request.user:
            raise PermissionDenied("You are not allowed to update this meal.")
        serializer.save()

    def perform_destroy(self, instance):
        """
        Allow deletions only by the owner of the meal's restaurant.
        """
        if instance.restaurant.user != self.request.user:
            raise PermissionDenied("You are not allowed to delete this meal.")
        instance.delete()


class FavoriteViewSet(viewsets.ModelViewSet):
    serializer_class = FavoriteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        Show the favorites of the authenticated user only.
        """
        return Favorite.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        """
        Add a meal to the authenticated user's favorites.
        """
        serializer.save(user=self.request.user)

    @action(detail=False, methods=['post'])
    def toggle(self, request):
        """
        Toggle the meal in the user's favorites.
        """
        meal_id = request.data.get('meal_id')
        
        if not meal_id:
            return Response({'detail': 'meal_id is required.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            meal = Meals.objects.get(id=meal_id)
        except Meals.DoesNotExist:
            return Response({'detail': 'Meal not found.'}, status=status.HTTP_404_NOT_FOUND)

        # Toggle the favorite status
        fav, created = Favorite.objects.get_or_create(user=request.user, meal=meal)

        if not created:
            fav.delete()
            return Response({'detail': 'Removed from favorites.'})
        return Response({'detail': 'Added to favorites.'})
