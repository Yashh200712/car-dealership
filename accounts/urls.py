from django.urls import path
from .views import login_view, register_view, dashboard, logout_view
from . import views

urlpatterns = [
    path('login/', login_view, name='login_view'),
    path('register/', register_view, name='register_view'),
    path('dashboard/', dashboard, name='dashboard'),
    path('logout/', logout_view, name='logout_view'),

    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('service/', views.services, name='service'),

    path('fleet/', views.fleet, name='fleet'),

    # Vehicle Details
    path('vehicle/<int:pk>/', views.vehicle_detail, name='vehicle_detail'),
]