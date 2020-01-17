import json

from django.shortcuts import render
from django.contrib import messages

from blog.models import Post
from about.models import Biography

from datetime import datetime
from dateutil import tz

from newsapi import NewsApiClient

# Create your views here.
# News API key - 4a*********************

with open('sta-config.json') as config_file:
        config = json.load(config_file)

def news_index(request):
    newsapi = NewsApiClient(api_key=config['NEWS_API_KEY'])
    local_time = tz.tzlocal()

    title = 'Top Tech Headlines'
    api = newsapi.get_top_headlines(category='technology', language='en', country='us')

    if request.method == 'GET' and 'search' in request.GET:
        keyword = request.GET['search']
        if keyword == '':
            messages.error(request, "It appears as though you didn't search for keywords. ")
        else:
            title = "Results for '" + keyword + "'"
            api = newsapi.get_everything(q=keyword, sort_by="relevancy", language='en')

    top_articles = api['articles']
    news = []
    author = []
    desc = []
    img = []
    url = []
    date = []

    for i in range(len(top_articles)):
        article = top_articles[i]
        news.append(article['title'])
        author.append(article['author'])
        desc.append(article['description'])
        img.append(article['urlToImage'])
        url.append(article['url'])
        fdate = datetime.strptime(article['publishedAt'], '%Y-%m-%dT%H:%M:%SZ')
        fdate = datetime.strftime(fdate, '%b %d, %Y')
        date.append(fdate)
    articles = zip(news, author, desc, img, url, date)

    recent_posts = Post.objects.all().order_by('-created_on')[:3]
    bios = Biography.objects.all()

    messages.info(request, 'Please pardon our appearance, this page is under construction.')

    return render(request, 'news_index.html', context ={'articles': articles, 'title': title, 'recent_posts': recent_posts, 'bios': bios,})
