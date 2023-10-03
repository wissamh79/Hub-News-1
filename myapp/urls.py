from . import views
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login, name="login"),
    path("news", views.news, name="news"),
    path("article/<int:article_id>", views.article, name="article"),
    path("categories", views.categories, name="categories"),
    path("category/<int:category_id>", views.category_page, name="category")
]
