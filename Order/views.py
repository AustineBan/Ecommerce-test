from django.shortcuts import render, redirect
from Cart.models import Cart, CartItem
from .models import Order, OrderItem

# Create your views here.
def checkout(request):
    cart = Cart.objects.get(user=request.user)
    order = Order.objects.create(user=request.user)
    for cart_item in cart.cart_items.all():
        order_item = OrderItem.objects.create(order=order, product=cart_item.product, user=request.user, discount=0, quantity=cart_item.quantity)
        cart_item.delete()

    return redirect("product:home")