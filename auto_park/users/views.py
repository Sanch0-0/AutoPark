from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import RegisterForm, LoginForm
from .models import User


def register_view(request):

    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            phone_number = form.cleaned_data["phone_number"]
            password = form.cleaned_data["password1"]

            user = User.objects.create_user(phone_number=phone_number, password=password)

            login(request, user)

            messages.success(request, "Registration successful. Welcome!")
            return redirect("home") 
    else:
        form = RegisterForm()

    return render(request, "register.html", {"form": form})


def login_view(request):
    
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            phone_number = form.cleaned_data["phone_number"]
            password = form.cleaned_data["password"]

            user = authenticate(request, phone_number=phone_number, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "You are now logged in.")
                return redirect("home")
            else:
                messages.error(request, "Invalid phone number or password.")
    else:
        form = LoginForm()

    return render(request, "login.html", {"form": form})


@login_required
def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect("login") 
