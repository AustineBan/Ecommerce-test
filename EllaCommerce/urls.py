from django.urls import path
from . import views

app_name = "product"
urlpatterns = [
    path('', views.home, name="home"),
    path('<slug:cate_slug>/', views.home_cate, name="cate"),
    path('detail/<int:product_id>/', views.detail, name="detail"),
]
