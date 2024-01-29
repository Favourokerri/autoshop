from django.contrib import admin
from .models import HeroSection

# Register your models here.
class HeroAdmin(admin.ModelAdmin):
    list_display=['title', 'description']

admin.site.register(HeroSection, HeroAdmin)