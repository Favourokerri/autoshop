from django.shortcuts import render
from socials.models import Socials

def socials(request):
    """ to make socials link avaliable throug out the pages"""
    socials = Socials.objects.filter().first()

    return {"socials": socials}