from django.db import models
from django.contrib.auth.models import User
from EllaCommerce.models import Product

# Create your models here.
class Cart(models.Model):
    user = models.OneToOneField(User, related_name="cart", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    @property
    def total(self):
        total = 0
        for cart_item in self.cart_items.all():
            total = total + cart_item.total()
        return total

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, related_name="cart_items", on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name="cart_item", on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name="cart_items", on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def total(self):
        return self.quantity * self.product.price