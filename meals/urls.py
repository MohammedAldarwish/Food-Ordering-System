from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
 
 
router = DefaultRouter()
router.register(r'favorites', views.FavoriteViewSet, basename='favorite')
router.register(r'meals', views.MealViewSet , basename='meal')

urlpatterns = [

    path('', include(router.urls))       
]