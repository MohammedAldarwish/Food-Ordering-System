from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
 
 
router = DefaultRouter()
router.register(r'favorites', views.FavoriteViewSet, basename='favorite')

urlpatterns = [
    path('', views.MealsListView.as_view(), name='meals-list-view'),
    path('create/', views.MealsCreateView.as_view(), name='meals-create'),

    path('api/', include(router.urls))       
]