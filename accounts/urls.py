from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from . import views


urlpatterns = [
    path("", views.UserCreateView.as_view(), name="user_create"),
    path("login/", views.UserLoginView.as_view(), name="user_login"),
    path("changepassword/", views.UserPasswordChangeView.as_view(), name="user_changepassword"),
    path("withdraw/", views.UserWithdrawalView.as_view(), name="user_withdrawal"),
    path("signin/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("<str:username>/", views.UserProfileView.as_view(), name="user_profile"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
