from django.shortcuts import render
from .models import Service

# Create your views here.
def service(request):
    """ view for services"""
    services = Service.objects.all()
    context = {"services": services}
    return render(request, 'pages/services.html', context)