from django.shortcuts import render
from django.contrib import messages
from home.models import Welcome, Testimonial
from blog.models import Post
from about.models import Biography

# Create your views here.

def home_index(request):
    welcome = Welcome.objects.all()[:1]
    testimonial = Testimonial.objects.all()
    recent_posts = Post.objects.all().order_by('-created_on')[:3]
    bios = Biography.objects.all()
    context = {
        'welcome' : welcome,
        'testimonial' : testimonial,
        'recent_posts': recent_posts,
        'bios': bios,
    }

    messages.info(request, 'Please pardon our appearance, this page is under construction.')

    return render(request, 'index.html', context)