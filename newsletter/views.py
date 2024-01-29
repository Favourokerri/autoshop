from django.shortcuts import render, redirect
from .models import NewsLetter
from django.contrib import messages

# Create your views here.
def newsletter(request):
    if request.method == "POST":
        email = request.POST.get('email')
        try:
            if not NewsLetter.objects.filter(email=email).exists():
                NewsLetter.objects.create(email=email)
                messages.success(request, "thanks for subscribing")
            else:
                messages.warning(request, "you have already subscribed")
            return redirect('home')
        except Exception as e:
            messages.error(request, 'sorry an error occured. try again later or contact us')
            return redirect('home')
