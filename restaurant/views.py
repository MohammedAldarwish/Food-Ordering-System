from django.forms import ValidationError
from rest_framework import viewsets
from .serializers import RestaurantSerializers
from .models import Restaurant
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action 
from rest_framework.response import Response
from rest_framework import status


class RestaurantView(viewsets.ModelViewSet):
    queryset = Restaurant.objects.filter(is_approved=True)
    serializer_class = RestaurantSerializers
    permission_classes = [IsAuthenticated]

    
    def perform_create(self, serializer):
        if Restaurant.objects.filter(user=self.request.user).exists():
            raise ValidationError('You can only create one restaurant.')
        serializer.save(user=self.request.user)
    
    
    @action(detail=False, methods=['delete'], url_path='delete-restaurant')
    def delete_my_restaurant(self, request):
        try:
            restaurant = Restaurant.objects.get(user=request.user)
            restaurant.delete()
            return Response({"detail": "Restaurant deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
        except Restaurant.DoesNotExist:
            return Response({"detail": "You don't have a restaurant to delete."}, status=status.HTTP_404_NOT_FOUND)

    @action(detail=False, methods=['put'], url_path='update-restaurant')
    def update_restaurant(self, request):
        try:
            restaurant = Restaurant.objects.get(user=request.user)
            serializer  = self.get_serializer(restaurant, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=400)
        except Restaurant.DoesNotExist:
            return Response({"detail": "You don't have a restaurant to update."}, status=404)
