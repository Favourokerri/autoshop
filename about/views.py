from django.shortcuts import render
from .models import AboutUs

# Create your views here.
def aboutUS(request):
    """ views for about """
    about = AboutUs.objects.filter().first()
    context = {"about": about}
    return render(request, 'pages/about.html', context)