from rest_framework import serializers

from .models import Cart, CartProduct


class CartProductSerializer(serializers.ModelSerializer):

    clothes_id = serializers.IntegerField(source="clothes.id")
    total = serializers.SerializerMethodField("get_total")

    def get_total(self, obj):
        return obj.clothes.price_with_discount * obj.quantity

    class Meta:
        model = CartProduct
        exclude = ['cart', 'clothes']


class CartSerializer(serializers.ModelSerializer):

    products = CartProductSerializer(many=True)
    user_id = serializers.IntegerField(source="user.id")

    class Meta:
        model = Cart
        exclude = ["user"]
