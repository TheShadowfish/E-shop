from django.core.cache import cache

from catalog.models import Version
from config import settings


def get_cashed_versions_for_products():
    if settings.CACHE_ENABLED:
        key = f'version_list'
        version_list = cache.get(key)
        if version_list is None:
            version_list = Version.objects.all()
            cache.set(key, version_list)
    else:
        version_list = Version.objects.all()
    return version_list

