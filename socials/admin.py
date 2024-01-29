from django.contrib import admin
from .models import Socials

# Register your models here.
class SocialsAdmin(admin.ModelAdmin):
    list_display = ['facebook_link', 'whatsapp_link']

admin.site.register(Socials, SocialsAdmin)