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
    products_count = serializers.SerializerMethodField("get_products_count")
    total_price = serializers.SerializerMethodField("get_total_price")
    total_price_with_discount = serializers.SerializerMethodField("get_total_price_with_discount")

    def get_products_count(self, obj):
        return obj.products_count

    def get_total_price(self, obj):
        return obj.total_price

    def get_total_price_with_discount(self, obj):
        return obj.total_price_with_discount


    class Meta:
        model = Cart
        exclude = ["user"]


class CartProductCreationSerializer(serializers.ModelSerializer):

    class Meta:
        model = CartProduct
        fields = [
            "cart",
            "clothes",
            "quantity"
        ]

    def validate_quantity(self, value):
        if value < 1 or value > 100:
            raise serializers.ValidationError("quantity must be greater than 0 and less or equal to 100")
        return value


class CartProductChangeQuantitySerializer(serializers.ModelSerializer):

    class Meta:
        model = CartProduct
        fields = [
            "quantity",
        ]

    def validate_quantity(self, value):
        if value < 1 or value > 100:
            raise serializers.ValidationError("quantity must be greater than 0 and less or equal to 100")

        return value
