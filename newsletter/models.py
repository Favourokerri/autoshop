from django.db import models

# Create your models here.
class NewsLetter(models.Model):
    """ models for newsletter"""
    email = models.CharField(max_length=200)

    def __str__(self):
        return self.email