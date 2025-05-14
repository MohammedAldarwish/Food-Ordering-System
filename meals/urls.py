from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
 
 
router = DefaultRouter()
router.register(r'favorites', views.FavoriteViewSet, basename='favorite')
<<<<<<< HEAD
router.register(r'meals', views.MealViewSet , basename='meal')

urlpatterns = [

    path('', include(router.urls))       
=======

urlpatterns = [
    path('', views.MealsListView.as_view(), name='meals-list-view'),
    path('create/', views.MealsCreateView.as_view(), name='meals-create'),

    path('api/', include(router.urls))       
>>>>>>> 384d072cae553316b277c547a712ba2176ce2416
]