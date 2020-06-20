from django.shortcuts import render
from newsapi import NewsApiClient

# my views here.
def Index(request):
    newsapi = NewsApiClient(api_key='feff2ee9bde243f4bb0852af6fdb2f9f')
    
    # top-headline
    top_headlines = newsapi.get_top_headlines(sources="al-jazeera-english")

    articles = top_headlines['articles']

    news = []
    desc = []
    img = []

    for i in range(len(articles)):
        myarticles = articles[i]

        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
    
    mylist = zip(news, desc, img)

    return render(request, 'index.html', context={"mylist":mylist})


def bbc(request):
    newsapi = NewsApiClient(api_key='feff2ee9bde243f4bb0852af6fdb2f9f')
        
    # top-headline
    top_headlines = newsapi.get_top_headlines(sources="bbc-news")
        
    articles = top_headlines['articles']
        
    news = []
    desc = []
    img = []
    
    for i in range(len(articles)):
        myarticles = articles[i]

        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
    
    mylist = zip(news, desc, img)

    return render(request, 'bbc.html', context={"mylist":mylist})