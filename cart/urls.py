from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import CartViewSet, CartItemViewSet

router = DefaultRouter()
<<<<<<< HEAD
router.register(r'', CartViewSet, basename='cart')
=======
router.register(r'cart', CartViewSet, basename='cart')
>>>>>>> 384d072cae553316b277c547a712ba2176ce2416
router.register(r'cart-items', CartItemViewSet, basename='cart-item')


urlpatterns = [
    path('', include(router.urls))

]