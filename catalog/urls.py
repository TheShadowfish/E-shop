from django.urls import path
from django.views.decorators.cache import cache_page

from catalog.apps import CatalogConfig

# home, product_detail,  product_detail, catalog, create
from catalog.views import (
    ProductListView,
    ProductDetailView,
    ProductCreateView,
    ProductUpdateView,
    ProductDeleteView,
    Product2ListView,
    Product3ListView,
    ContactsPageViews,
    VersionListView,
    VersionDetailView,
    VersionCreateView,
    VersionUpdateView,
    VersionDeleteView,
)

app_name = CatalogConfig.name

urlpatterns = [
    path("", ProductListView.as_view(), name="home"),
    path("contacts/", ContactsPageViews.as_view(), name="contacts"),
    path("products/<int:pk>/", cache_page(60)(ProductDetailView.as_view()), name="product_detail"),
    path("home/paginate_by_2/", Product2ListView.as_view(), name="home_paginate_by_2"),
    path("home/paginate_by_3/", Product3ListView.as_view(), name="home_paginate_by_3"),
    path("create/", ProductCreateView.as_view(), name="create"),
    path(
        "product/<int:pk>/update/", ProductUpdateView.as_view(), name="product_update"
    ),
    path(
        "product/<int:pk>/delete/", ProductDeleteView.as_view(), name="product_delete"
    ),
    path("versions/", VersionListView.as_view(), name="versions"),
    path("versions/<int:pk>/", VersionDetailView.as_view(), name="version_detail"),
    path("version_create/", VersionCreateView.as_view(), name="version_create"),
    path(
        "version/<int:pk>/update/", VersionUpdateView.as_view(), name="version_update"
    ),
    path(
        "version/<int:pk>/delete/", VersionDeleteView.as_view(), name="version_delete"
    ),
]
