from django.urls import path
from .views import service

urlpatterns = [
    path('services/', service, name="services")
]
