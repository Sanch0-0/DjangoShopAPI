from rest_framework.generics import ListAPIView, RetrieveAPIView

from .models import Category, Clothes
from .serializers import ClothesSerializer, CategorySerializer



class ClothesListAPIView(ListAPIView):

    queryset = Clothes.objects.all()
    serializer_class = ClothesSerializer


class CategoryListAPIView(ListAPIView):

    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ClothesRetrieveAPIVIew(RetrieveAPIView):

    queryset = Clothes.objects.all()
    serializer_class = ClothesSerializer

class CategoryRetrieveAPIVIew(RetrieveAPIView):

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
