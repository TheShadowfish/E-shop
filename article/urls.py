from django.urls import path
from article.apps import ArticleConfig
from article.views import ArticleListView, ArticleDetailView, ArticleCreateView, ArticleUpdateView, ArticleDeleteView

app_name = ArticleConfig.name

urlpatterns = [
    path('blog', ArticleListView.as_view(), name='blog'),
    path('article/<int:pk>/', ArticleDetailView.as_view(), name='article_detail'),
    path('article_create/', ArticleCreateView.as_view(), name='article_create'),
    path('article/<int:pk>/update/', ArticleUpdateView.as_view(), name='article_update'),
    path('article/<int:pk>/delete/', ArticleDeleteView.as_view(), name='article_delete'),
]
