from django.db import models

# Create your models here.
class Socials(models.Model):
    facebook_link = models.URLField(blank=True, null=True, help_text='can be left blank')
    instagram_link = models.URLField(blank=True, null=True, help_text='can be left blank')
    twitter_link = models.URLField(blank=True, null=True, help_text='can be left blank')
    whatsapp_link = models.URLField(blank=True, null=True, help_text='can be left blank')

    def __str__(self):
        return self.facebook_link