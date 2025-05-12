from rest_framework import status
from rest_framework.response import Response
from .models import Meals , Favorite
from .serializers import MealSerializer, FavoriteSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from restaurant.models import Restaurant
from .filters import MealFilter
from rest_framework import viewsets
from rest_framework.decorators import action


class MealsCreateView(APIView):
    permission_classes = [IsAuthenticated]
    

    def post(self, request):
        try:
            restaurant = request.user.restaurant 
        except Restaurant.DoesNotExist:
            return Response({"detail": "You must have a restaurant to add meals."}, status=status.HTTP_400_BAD_REQUEST)
        
        meal_data = request.data
        meal_data['restaurant'] = restaurant.id

        meal_serializer = MealSerializer(data=meal_data)

               

        if meal_serializer.is_valid():
            meal_serializer.save(added_by=request.user)
            return Response(meal_serializer.data, status=status.HTTP_201_CREATED)
        return Response(meal_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class MealsListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        meals = Meals.objects.filter(is_available=True)

        meal_filter = MealFilter(request.query_params, queryset=meals)
        meals = meal_filter.qs

        serializer = MealSerializer(meals, many=True)
        return Response(serializer.data)

class FavoriteViewSet(viewsets.ModelViewSet):
    serializer_class = FavoriteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Favorite.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


    @action(detail=False, methods=['post'])
    def toggle(self, request):
        meal_id = request.data.get('meal_id')
        if not meal_id:
            return Response({'detail': 'meal_id is required.'}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            meal = Meals.objects.get(id=meal_id)
        except Meals.DoesNotExist:
            return Response({'detail': 'Meal not found.'}, status=status.HTTP_404_NOT_FOUND)
        
        fav, created = Favorite.objects.get_or_create(user=request.user, meal=meal)

        if not created:
            fav.delete()
            return Response({'detail': 'Removed from favorites.'})
        return Response({'detail': 'Added to favorites.'})
