from django.shortcuts import render
from django.contrib import messages
from home.models import Welcome, Testimonial

# Create your views here.

def home_index(request):
    welcome = Welcome.objects.all()[:1]
    testimonial = Testimonial.objects.all()
    context = {
        'welcome' : welcome,
        'testimonial' : testimonial
    }

    messages.info(request, 'Please pardon our appearance, this page is under construction.')

    return render(request, 'index.html', context)