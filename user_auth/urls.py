from django.urls import path
from .views import *
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
     path('token/refresh', TokenRefreshView.as_view(), name='token-refresh'),
    path('register/', UserRegisterAPIView.as_view(), name = 'register'),
    path('login/', LoginAPIView.as_view(), name = 'login'),
    path('profile/', UserProfileAPIView.as_view(), name = 'profile'),
    path('index/', index, name = 'index'),
]

