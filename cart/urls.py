from django.urls import path

from .views import (
    CartAPIView,
    CartProductCreateAPIView,
    CartProductDeleteAPIVIew,
    CartProductChangeQuantityAPIView,
)

urlpatterns = [
    path("", CartAPIView.as_view()),
    path("add/", CartProductCreateAPIView.as_view()),
    path("delete/<int:pk>", CartProductDeleteAPIVIew.as_view()),
    path("product/<int:pk>/quantity/", CartProductChangeQuantityAPIView.as_view()),
]
