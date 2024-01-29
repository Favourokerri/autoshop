# admin.py
from django.contrib import admin
from .models import Service, Icon

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ['name']

admin.site.register(Service, ServiceAdmin)
admin.site.register(Icon)
