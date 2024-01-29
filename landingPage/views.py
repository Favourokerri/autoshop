from django.shortcuts import render
from .models import HeroSection
from services.models import Service
from contact.models import ContactInfo

# Create your views here.
def homePage(request):
    """ view for home page"""
    heroSection = HeroSection.objects.all()
    featured_services = Service.objects.filter(featured=True)
    contact = ContactInfo.objects.filter().first()
    context={"heroSection": heroSection,
             "featured_services": featured_services,
             "contact": contact,}
    return render(request, 'pages/home.html', context)

def custom_404_view(request, exception):
    return render(request, 'error/404.html', status=404)

def custom_500_view(request):
    return render(request, 'error/500.html', status=500)