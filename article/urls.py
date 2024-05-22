from django.urls import path
from article.apps import ArticleConfig
from catalog.views import contacts
# home, product_detail,  product_detail, catalog, create
from article.views import ArticleListView, ArticleDetailView, ArticleCreateView, ArticleUpdateView, ArticleDeleteView

app_name = ArticleConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='home'),
    path('contacts/', ContactsPageViews.as_view(), name='contacts'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('home/paginate_by_2/', ProductPaginate2ListView.as_view(), name='home_paginate_by_2'),
    path('home/paginate_by_3/', ProductPaginate3ListView.as_view(), name='home_paginate_by_3'),
    path('create/', ProductCreateView.as_view(), name='create'),
    path('product/<int:pk>/update/', ProductUpdateView.as_view(), name='product_update'),
    path('product/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),
]
