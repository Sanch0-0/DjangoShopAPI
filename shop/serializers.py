from rest_framework import serializers

from .models import Clothes, Category


class ClothesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Clothes
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"
