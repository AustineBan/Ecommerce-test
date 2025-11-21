from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("<h1>Welcome to our home page</h1>")
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')