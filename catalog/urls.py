from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import home, contacts, product_detail, catalog

app_name = CatalogConfig.name

urlpatterns = [
    path('', home, name='home'),
    path('contacts/', contacts, name='contacts'),
    path('products/<int:pk>/', product_detail, name='product_detail'),
    path('catalog/<int:per_page>/<int:page>/', catalog, name='catalog'),
    path('products/<int:pk>/<int:per_page>/<int:page>/', product_detail, name='product_detail'),
]
