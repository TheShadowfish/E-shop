from article.models import Article
from catalog.forms import StyleFormMixin
from django import forms


class ArticleForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Article
        fields = (
            "name",
            "body",
            "image",
            "is_published",
            "views_count",
        )
