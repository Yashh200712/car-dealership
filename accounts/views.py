from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages         
from .models import Enquiry
from .models import Vehicle
from django.shortcuts import render

def vehicle_detail(request, pk):

    vehicles = {
        1: {
            "name": "BMW M4",
            "price": "₹1.50 Cr",
            "image": "https://images.unsplash.com/photo-1555215695-3004980ad54e",
            "description": "Luxury performance coupe with exceptional handling and power."
        },
        2: {
            "name": "Audi RS7",
            "price": "₹2.20 Cr",
            "image": "https://images.unsplash.com/photo-1492144534655-ae79c964c9d7",
            "description": "Premium sports sedan with stunning performance and comfort."
        }
    }

    vehicle = vehicles.get(pk)

    return render(
        request,
        'accounts/vehicle_detail.html',
        {'vehicle': vehicle}
    )


def home(request):
    return render(request, "accounts/home.html")


def about(request):
    return render(request, "accounts/about.html")

def services(request):
    return render(request, "accounts/service.html")

def fleet(request):
    vehicles = Vehicle.objects.all()
    return render(request, 'accounts/fleet.html', {
        'vehicles': vehicles
    })

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

