from django.shortcuts import render
from django.contrib import messages

from datetime import datetime
from dateutil import tz

from newsapi import NewsApiClient

# Create your views here.
# News API key - 4a168c464f74480aa143afd5ce73b476

def news_index(request):
    newsapi = NewsApiClient(api_key='4a168c464f74480aa143afd5ce73b476')
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


    messages.info(request, 'Please pardon our appearance, this page is under construction.')

    return render(request, 'news_index.html', context ={'articles': articles, 'title': title})
