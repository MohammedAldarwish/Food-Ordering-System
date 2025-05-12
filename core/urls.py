from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token-obtain-pair-view'),
    path('api/refresh/', TokenRefreshView.as_view(), name='token-refresh-view'),
    path('api/account/', include('accounts.urls')),
    path('api/restaurant/', include('restaurant.urls')),
    path('api/meals/', include('meals.urls')),
    path('api/cart/', include('cart.urls')),
    path('api/checkout/', include('order.urls'))
]
