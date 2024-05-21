from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import contacts, product_detail, catalog, create
# home, product_detail
from catalog.views import ProductListView, ProductDetailView

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='home'),
    path('contacts/', contacts, name='contacts'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('catalog/<int:per_page>/<int:page>/', catalog, name='catalog'),
    path('products/<int:pk>/<int:per_page>/<int:page>/', product_detail, name='product_detail'),
    path('create/', create, name='create'),
]
