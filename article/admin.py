from django.contrib import admin
from article.models import Article, Tag


# Register your models here.
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
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


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('title','article',)
    list_filter = ('article',)