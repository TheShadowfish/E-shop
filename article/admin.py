from django.contrib import admin
from article.models import Article

# Register your models here.
@admin.register(Article)
class ProductAdmin(admin.ModelAdmin):
    list_display = fields = ("id",
        "name",
        "slug",
        "body",
        "image",
        "created_at",
        "is_published",
        "views_count",
    )
    list_filter = ("name",)
    search_fields = ("name", "is_published")