from django.contrib import admin
from .models import ContactInfo, ContactMessage

# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    list_display = ['email', 'phone_number', 'location']

class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email',)
    search_fields = ('email',)

admin.site.register(ContactMessage, ContactMessageAdmin)
admin.site.register(ContactInfo, ContactAdmin)
