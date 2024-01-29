from django.db import models

# Create your models here.
class AboutUs(models.Model):
    """ about us model"""
    about = models.TextField()

    def __str__(self):
        return self.about