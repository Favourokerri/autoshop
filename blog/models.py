from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField  # Assuming you are using CKEditor for the RichTextField

class Blog(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='blog_images/')
    content = RichTextField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title