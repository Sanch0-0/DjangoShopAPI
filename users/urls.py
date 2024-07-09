from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .views import (
    RegistrationAPIView,
    UpdateProfileAPIView
)


urlpatterns = [
    path("registration/", RegistrationAPIView.as_view()),
    path("token/", TokenObtainPairView.as_view()),
    path("token/refresh/", TokenRefreshView.as_view()),
    path("update/", UpdateProfileAPIView.as_view()),
]
