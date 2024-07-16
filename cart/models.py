from django.db import models

from shop.models import Clothes

class Cart(models.Model):
    user = models.OneToOneField("users.User", on_delete=models.CASCADE, related_name="cart")
    created_at = models.DateTimeField(verbose_name="creation date", auto_now_add=True)

    @property
    def products_count(self) -> int:
        products = self.products.values_list("quantity", flat=True)
        return sum(products)

    @property
    def total_price_with_discount(self):
        total = 0
        for product in self.products.all():
            total += product.clothes.price_with_discount * product.quantity
        return total

    @property
    def total_price(self):
        products = self.products.values_list("clothes__price", "quantity")
        return sum(map(lambda product: product[0] * product[1], products))



class CartProduct(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="products")
    clothes = models.ForeignKey(Clothes, on_delete=models.CASCADE, related_name="products")
    quantity = models.SmallIntegerField(verbose_name="quantity", default=1)
