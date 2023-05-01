from django.contrib import admin
from .models import *

class ServiceAdmin(admin.ModelAdmin):
    list_display = ['title', 'price']

admin.site.register(Service, ServiceAdmin)