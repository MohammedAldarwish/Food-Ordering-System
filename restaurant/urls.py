from django.urls import path, include 
from rest_framework.routers import DefaultRouter
from .views import RestaurantView

router = DefaultRouter()
<<<<<<< HEAD
router.register(r'', RestaurantView)
=======
router.register(r'restaurant', RestaurantView)
>>>>>>> 384d072cae553316b277c547a712ba2176ce2416

urlpatterns = [
    path('', include(router.urls))
]