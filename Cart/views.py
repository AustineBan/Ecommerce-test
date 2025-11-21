from django.shortcuts import render, redirect
from .models import Cart, CartItem
from EllaCommerce.models import Product
from django.http import JsonResponse


# Create your views here.
def add_to_cart(request, product_id):
    if request.method == 'POST':
        if request.user.is_authenticated:
            product = Product.objects.get(id=product_id)
            cart = None
            cart_item = None
            try:
                cart = Cart.objects.get(user=request.user)
            except Cart.DoesNotExist:
                cart = Cart.objects.create(user=request.user)
            try:
                cart_item = CartItem.objects.get(product=product, user=request.user, cart=cart)
                cart_item.quantity = cart_item.quantity + 1
                cart_item.save()
            except CartItem.DoesNotExist:
                cart_item = CartItem.objects.create(product=product, cart=cart, user=request.user, quantity=1)

            resp = {
                "success": True,
                "product": product.name
            }
            return JsonResponse(resp)
        else:
            return redirect("login")
    return redirect("product:home")

def view_cart(request):
    cart = None
    cart_items = None
    try:
        cart = Cart.objects.get(user=request.user)
    except Cart.DoesNotExist:
        cart = Cart.objects.create(user=request.user)

    cart_items = CartItem.objects.filter(user=request.user, cart=cart)
    
    return render(request, 'cart/index.html', {"cart_items": cart_items, "cart": cart})

def increase_quantity(request, cart_id):
    cart_item = CartItem.objects.get(id=cart_id)
    cart_item.quantity = cart_item.quantity + 1
    cart_item.save()
    return redirect("cart:view_cart")

def decrease_quantity(request, cart_id):
    cart_item = CartItem.objects.get(id=cart_id)
    cart_item.quantity = cart_item.quantity - 1

    if cart_item.quantity <= 1:
        cart_item.quantity = 1
    cart_item.save() 
    return redirect("cart:view_cart")

def delete_cart_item(request, cart_id):
    cart_item = CartItem.objects.get(id=cart_id)
    cart_item.delete()
    return redirect("cart:view_cart")
