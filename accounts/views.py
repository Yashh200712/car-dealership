from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages         
from .models import Enquiry


def home(request):
    return render(request, "accounts/home.html")


def about(request):
    return render(request, "accounts/about.html")

def services(request):
    return render(request, "accounts/service.html")

def fleet(request):
    return render(request, 'accounts/fleet.html')


def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        vehicle = request.POST.get("vehicle")
        message = request.POST.get("message")

        Enquiry.objects.create(
            name=name,
            email=email,
            phone=phone,
            vehicle=vehicle,
            message=message
        )

        messages.success(request, "Your enquiry has been submitted successfully!")
        return redirect("contact")

    return render(request, "accounts/contact.html")


@login_required(login_url='login_view')
def dashboard(request):
    return render(request, "accounts/dashboard.html")


def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            messages.success(request, "Logged in successfully")
            return redirect('dashboard')

        messages.error(request, "Invalid username or password")

    return render(request, "accounts/login.html")


def register_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == "POST":
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:
            messages.error(request, "Passwords do not match")
            return redirect('register_view')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect('register_view')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists")
            return redirect('register_view')

        User.objects.create_user(
            username=username,
            first_name=firstname,
            last_name=lastname,
            email=email,
            password=password
        )

        messages.success(request, "Registration successful. Please login.")
        return redirect('login_view')

    return render(request, "accounts/register.html")


@login_required(login_url='login_view')
def logout_view(request):
    logout(request)
    messages.success(request, "Logged out successfully")
    return redirect('home')

