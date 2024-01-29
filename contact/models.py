# models.py
from django.db import models

class ContactInfo(models.Model):
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    location = models.CharField(max_length=255)

    def __str__(self):
        return f'Contact Information - Email: {self.email}, Phone: {self.phone_number}, Location: {self.location}'

class ContactMessage(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return self.name