from django.urls import path, include 
from rest_framework.routers import DefaultRouter
from .views import RestaurantView

router = DefaultRouter()
router.register(r'restaurant', RestaurantView)

urlpatterns = [
    path('', include(router.urls))
]