from django.shortcuts import render, get_object_or_404
from .models import Blog

# Create your views here.
def blog(request):
    """ blog view """
    blogs = Blog.objects.all()
    context={"blogs": blogs}
    return render(request, 'pages/blog.html', context)

def blog_post_detail(request, post_id):
    """Blog post detail view"""
    blog_post = get_object_or_404(Blog, id=post_id)
    recent_blogs = Blog.objects.exclude(id=post_id).order_by('-created_at')[:3]

    context = {"blog_post": blog_post, "recent_blogs": recent_blogs}
    return render(request, 'pages/blog_post.html', context)