from django.contrib import admin
from .models import Enquiry, Vehicle

@admin.register(Enquiry)
class EnquiryAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'vehicle', 'created_at']
    search_fields = ['name', 'email', 'vehicle']
    list_filter = ['created_at', 'vehicle']


@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ['name', 'brand', 'price']
    search_fields = ['name', 'brand']