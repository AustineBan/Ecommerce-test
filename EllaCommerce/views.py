from django.shortcuts import render
from .models import Product, Category

# Create your views here.
def home(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    product = Product.objects.get(id=2)
    return render(request, 'Ella/index.html', {"products": products, "categories": categories})

def home_cate(request, cate_slug):
    category = Category.objects.get(slug=cate_slug)
    products = Product.objects.filter(category=category)
    categories = Category.objects.all()
    return render(request, 'Ella/index.html', {'products': products, "category": category, "categories": categories})


def detail(request, product_id):
    product = Product.objects.get(id=product_id)
    return render(request, 'Ella/detail.html', {"product": product})