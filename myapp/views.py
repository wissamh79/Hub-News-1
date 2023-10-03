from django.shortcuts import render
from .models import User, category, articles, comments, subscriptions

# Create your views here.

def index(request):
  cats = category.objects.all()
  return render(request, 'index.html', {
    'cats': cats,
  })

def news(request):
  cats = category.objects.all()
  art = articles.objects.all()
  return render(request, 'news.html', {
    'cats': cats,
    'articles': art
  })

def article(request, article_id):
  cats = category.objects.all()
  article = articles.objects.get(pk=article_id)
  return render(request, 'article.html', {
    'cats': cats,
    'article': article
  })

def category_page(request, category_id):
  cats = category.objects.all()
  return render(request, 'category.html', {
    'cats': cats,
  })
  
def categories(request):
  cats = category.objects.all()
  return render(request, 'categories.html', {
    'cats': cats,
  })
  

def login(request):
  cats = category.objects.all()
  return render(request, 'login.html',{
    'cats': cats,
  })