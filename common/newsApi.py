from newsapi import NewsApiClient
from decouple import config

def get_news(**kwargs):
    newsapi = NewsApiClient(api_key=f"{config("NEWS_API_KEY")}")
    all_articles = newsapi.get_everything(**kwargs)
    return all_articles.get("articles")

