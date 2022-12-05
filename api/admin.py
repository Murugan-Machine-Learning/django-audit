from django.contrib import admin
from .models import UdyamForm
# Register your models here.

class UdyamFormAdmin(admin.ModelAdmin):
    list_display =  ('name', 'email', 'mobile','pan','aadhaar')

admin.site.register(UdyamForm, UdyamFormAdmin)