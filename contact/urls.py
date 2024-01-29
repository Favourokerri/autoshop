from django.urls import path
from .views import contact, contactUs

urlpatterns = [
    path('contact/', contact, name="contact"),
     path('contactMessage/', contactUs, name="contactMessage"),
]
