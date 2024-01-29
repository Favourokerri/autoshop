from django.shortcuts import render, redirect
from.models import ContactMessage, ContactInfo
from django.contrib import messages

# Create your views here.
def contact(request):
    """ view for contact"""
    contact = ContactInfo.objects.filter().first()
    context = {"contact": contact}
    return render(request, 'pages/contact.html', context)

def contactUs(request):
    """ contact messages"""
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        try:
            contact_message = ContactMessage(name=name, email=email, message=message)
            contact_message.save()
            messages.success(request, 'your message was sent successfully')
            return redirect('home')
        except Exception as e:
            messages.error(request, 'sorry an error occured')
    return render(request, 'pages/contact.html')