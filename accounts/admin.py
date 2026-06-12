from django.contrib import admin
from .models import Enquiry

# Register your models here.
from .models import Enquiry

@admin.register(Enquiry)
class EnquiryAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'vehicle', 'created_at']
    search_fields = ['name', 'email', 'vehicle']
    list_filter = ['created_at', 'vehicle']