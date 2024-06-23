from django.urls import path
from article.apps import ArticleConfig
from catalog.views import contacts

# home, product_detail,  product_detail, catalog, create
from article.views import (
    ArticleListView,
    ArticleDetailView,
    ArticleCreateView,
    ArticleUpdateView,
    ArticleDeleteView,
)

app_name = ArticleConfig.name

urlpatterns = [
    path("blog", ArticleListView.as_view(), name="blog"),
    path("article/<slug:slug>/", ArticleDetailView.as_view(), name="article_detail"),
    path("article_create/", ArticleCreateView.as_view(), name="article_create"),
    path(
        "article/<slug:slug>/update/", ArticleUpdateView.as_view(), name="article_update"
    ),
    path(
        "article/<slug:slug>/delete/", ArticleDeleteView.as_view(), name="article_delete"
    ),
]
