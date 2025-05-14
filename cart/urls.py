from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import CartViewSet, CartItemViewSet

router = DefaultRouter()
router.register(r'', CartViewSet, basename='cart')
router.register(r'cart-items', CartItemViewSet, basename='cart-item')


urlpatterns = [
    path('', include(router.urls))

]