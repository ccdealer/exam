from django.contrib import admin

# Register your models here.
from news.models import Article

admin.site.register(Article)