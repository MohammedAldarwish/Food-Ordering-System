from rest_framework import viewsets
from .serializers import RestaurantImageSerializers, RestaurantSerializers
from .models import Restaurant, RestaurantImage
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

class RestaurantView(viewsets.ModelViewSet):
    queryset = Restaurant.objects.filter(is_approved=True)
    serializer_class = RestaurantSerializers
    permission_classes = [IsAuthenticated]

    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

