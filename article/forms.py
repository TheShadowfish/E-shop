from django import forms

from article.models import Article


class ArticleForm(forms.ModelForm):


    class Meta:
        model = Article
        fields = '__all__'
        # fields = (
        #     "name",
        #     "body",
        #     "image",
        #     "created_at",
        #     "is_published",
        #     "views_count",
        # )
        exclude = ('views_count','slug',)