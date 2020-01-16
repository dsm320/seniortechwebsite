from django.shortcuts import render
from django.contrib import messages
from about.models import About, Biography
from blog.models import Post

# Create your views here.

def about_index(request):
    about = About.objects.all()[:1]
    bios = Biography.objects.all()
    recent_posts = Post.objects.all().order_by('-created_on')[:3]
    context = {
        'about': about,
        'bios': bios,
        'recent_posts': recent_posts,
    }

    messages.info(request, 'Please pardon our appearance, this page is under construction.')

    return render(request, 'about.html', context)