from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages

from blog.forms import CommentForm
from blog.models import Post, Comment

# Create your views here.

""" A view to render all blog posts """
def blog_index(request):
    posts = Post.objects.all().order_by('-created_on')
    context = {
        'posts' : posts,
    }

    messages.info(request, 'Please pardon our appearance, this page is under construction.')

    return render(request, 'blog_index.html', context)

""" A view to render all blog categories """
def blog_category(request, category):
    posts = Post.objects.filter(
        categories__name__contains=category
    ).order_by(
        '-created_on'
    )
    context = {
        'category' : category,
        'posts' : posts,
    }
    return render(request, 'blog_category.html', context)

""" A view to render a specific blog post """
def blog_detail(request, pk):
    post = Post.objects.get(pk=pk)
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author=form.cleaned_data["author"],
                body=form.cleaned_data["body"],
                post=post
            )
            comment.save()
            return HttpResponseRedirect(reverse('blog_detail', args=[post.pk]))

    comments = Comment.objects.filter(post=post).order_by('-created_on')
    context = {
        "post": post,
        "comments": comments,
        "form": form,
    }
    return render(request, "blog_detail.html", context)