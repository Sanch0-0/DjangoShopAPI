from django.urls import path

from .views import (
    ClothesListAPIView,
    ClothesRetrieveAPIVIew,
    CategoryListAPIView,
    CategoryRetrieveAPIVIew,
)

urlpatterns = [
    path("clothes/", ClothesListAPIView.as_view()),
    path("clothes/<int:pk>", ClothesRetrieveAPIVIew.as_view()),
    path("categories/", CategoryListAPIView.as_view()),
    path("categories/<int:pk>", CategoryRetrieveAPIVIew.as_view()),
]
