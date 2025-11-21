from django.urls import path
from . import views

app_name = "cart"

urlpatterns = [
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name="add_to_cart"),
    path('cart_items/', views.view_cart, name="view_cart"),
    path("increase/<int:cart_id>/", views.increase_quantity, name="increase"),
    path("decrease/<int:cart_id>/", views.decrease_quantity, name="decrease"),
    path("delete/<int:cart_id>/", views.delete_cart_item, name="delete")
]
