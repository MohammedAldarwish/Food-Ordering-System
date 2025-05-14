from django.urls import path
from . import views

urlpatterns = [
<<<<<<< HEAD
    path('', views.CheckoutView.as_view(), name='checkout')
=======
    path('checkout/', views.CheckoutView.as_view(), name='checkout')
>>>>>>> 384d072cae553316b277c547a712ba2176ce2416
]