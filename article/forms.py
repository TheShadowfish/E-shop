from django import forms

from article.models import Article, Tag

class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

class ArticleForm(StyleFormMixin, forms.ModelForm):


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
        exclude = ('views_count','slug','is_published',)



    def clean(self):
        cleaned_data = self.cleaned_data['name']
        if str(cleaned_data).isdigit():
            raise forms.ValidationError("Название статьи не должно состоять из одних цифр")


class TagForm(StyleFormMixin, forms.ModelForm):

    class Meta:
        model = Tag
        fields = '__all__'

