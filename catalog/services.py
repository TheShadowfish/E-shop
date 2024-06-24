from django.core.cache import cache

from catalog.models import Version, Category
from config import settings


def get_cached_versions_for_products():
    if settings.CACHE_ENABLED:
        key = f'version_list'
        version_list = cache.get(key)
        if version_list is None:
            version_list = Version.objects.all()
            cache.set(key, version_list)
    else:
        version_list = Version.objects.all()
    return version_list

def get_cached_category():
    if settings.CACHE_ENABLED:
        key = f'category_list'
        category_list = cache.get(key)
        if category_list is None:
            category_list = Category.objects.all()
            cache.set(key, category_list)
    else:
        category_list = Category.objects.all()
    return category_list

#
# def get_cached_category_for_product(object_pk):
#     if settings.CACHE_ENABLED:
#         key = f'category_list_{object_pk}'
#         category_list = cache.get(key)
#         if category_list is None:
#             category_list = Category.objects.filter()
#             cache.set(key, category_list)
#     else:
#         category_list = Category.objects.all()
#     return category_list