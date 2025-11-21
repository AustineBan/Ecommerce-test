from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')

    return render(request, 'login.html')

def register_view(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        first_name = request.POST.get("first-name")
        last_name = request.POST.get("last-name")
        email = request.POST.get("email")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        validation_obj = validate_user(username,email, password1, password2)
        if validation_obj["is_error"]:
            return render(request, 'register.html', {"error_messages": validation_obj["error_messages"]})
        
        user = User.objects.create_user(username=username, password=password1, first_name=first_name, last_name=last_name, email=email)

        if user is not None:
            return redirect('login')


    return render(request, 'register.html')

def validate_user(username,email, password1, password2):
    error_messages = []
    is_error = False
    if password1 != password2:
        error_messages.append("password and confirm password must match")
        is_error = True
    if User.objects.filter(username=username):
        error_messages.append("Username has been taken")
        is_error = True
    if User.objects.filter(email=email):
        error_messages.append("Email has been taken")
        is_error = True
    if username in password1:
        error_messages.append("Password is too weak")
        is_error = True
    if len(password1) < 8:
        error_messages.append("Password can't be less than 8")
        is_error = True

    return {
        "error_messages": error_messages,
        "is_error": is_error
    }

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login')