from django.shortcuts import render
from django.contrib import messages
from about.models import About

# Create your views here.

def about_index(request):
    about = About.objects.all()[:1]
    context = {
        'about' : about,
    }

    messages.info(request, 'Please pardon our appearance, this page is under construction.')

    return render(request, 'about.html', context)