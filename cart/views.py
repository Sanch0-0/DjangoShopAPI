from rest_framework import status, response
from rest_framework.generics import RetrieveAPIView, GenericAPIView
from rest_framework.permissions import IsAuthenticated

from .models import Cart, CartProduct
from .serializers import CartSerializer


class CartAPIView(RetrieveAPIView):

    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user.cart

    def delete(self, request):
        self.request.user.cart.products.all().delete()
        return response.Response(status=status.HTTP_204_NO_CONTENT)
