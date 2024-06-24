from django.core.cache import cache

from catalog.models import Version, Category, Product
from config import settings


def get_cached_versions_for_products(recached: bool = False):
    if settings.CACHE_ENABLED:
        key = f'version_list'
        if recached:
            version_list = Version.objects.all()
            cache.set(key, version_list)
        else:
            version_list = cache.get(key)
            if version_list is None:
                version_list = Version.objects.all()
                cache.set(key, version_list)
    else:
        version_list = Version.objects.all()
    return version_list


def get_cached_category(recached: bool = False):
    if settings.CACHE_ENABLED:
        key = f'category_list'
        if recached:
            category_list = Category.objects.all()
            cache.set(key, category_list)
        else:
            category_list = cache.get(key)
            if category_list is None:
                category_list = Category.objects.all()
                cache.set(key, category_list)
    else:
        category_list = Category.objects.all()
    return category_list


def get_cached_products(recached: bool = False):
    if settings.CACHE_ENABLED:
        key = f'products_list'
        if recached:
            product_list = Product.objects.all()
            cache.set(key, product_list)
        else:
            product_list = cache.get(key)
            if product_list is None:
                product_list = Product.objects.filter()
                cache.set(key, product_list)
    else:
        product_list = Product.objects.all()
    return product_list
