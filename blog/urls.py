from django.urls import path
from .views import blog, blog_post_detail

urlpatterns = [
    path('blog/', blog, name="blog"),
    path('blog/<int:post_id>/', blog_post_detail, name='blog_post'),
]
