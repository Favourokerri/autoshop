from django.urls import path
from .views import aboutUS

urlpatterns = [
    path('about/', aboutUS, name="about")
]
