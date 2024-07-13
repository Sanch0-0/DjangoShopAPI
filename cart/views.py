from rest_framework import status, response
from rest_framework.generics import RetrieveAPIView, CreateAPIView, DestroyAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import ValidationError

from .models import Cart, CartProduct
from .serializers import CartSerializer, CartProductCreationSerializer, CartProductChangeQuantitySerializer
from .permissions import IsOwner


class CartAPIView(RetrieveAPIView):

    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user.cart

    def delete(self, request):
        self.request.user.cart.products.all().delete()
        return response.Response(status=status.HTTP_204_NO_CONTENT)


class CartProductCreateAPIView(CreateAPIView):

    queryset = CartProduct.objects.all()
    serializer_class = CartProductCreationSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        cart_id = request.data['cart']
        if cart_id != request.user.cart.id:
            raise ValidationError({
                "cart": "Permission to this cart denied"
            }, code=400)

        clothes_id = serializer.validated_data['clothes']
        cart_product = request.user.cart.products.filter(clothes=clothes_id).first()
        if cart_product is not None:
            cart_product.quantity += serializer.validated_data['quantity']
            cart_product.save()
            return response.Response(data=serializer.data, status=status.HTTP_201_CREATED)

        return super().post(request, *args, **kwargs)


class CartProductDeleteAPIVIew(DestroyAPIView):

    queryset = CartProduct.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]


class CartProductChangeQuantityAPIView(UpdateAPIView):

    queryset = CartProduct.objects.all()
    serializer_class = CartProductChangeQuantitySerializer
    permission_classes = [IsAuthenticated, IsOwner]

