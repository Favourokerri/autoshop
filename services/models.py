# models.py
from django.db import models

class Icon(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    icon = models.ForeignKey(Icon, on_delete=models.SET_NULL, null=True, blank=True)
    featured = models.BooleanField(help_text="mark to display in home page", default=False)

    def __str__(self):
        return self.name