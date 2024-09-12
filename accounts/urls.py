from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import UserCreateView, UserLoginView

urlpatterns = [
    path("", UserCreateView.as_view(), name="user_create"),
    path("login/", UserLoginView.as_view(), name="user_login"),
    # path("signin/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
