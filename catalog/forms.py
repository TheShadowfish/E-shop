from django import forms
from django.forms import BooleanField

from catalog.models import Product, Contact, Version


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, BooleanField):
                field.widget.attrs['class'] = 'form-check-input'
            else:
                field.widget.attrs['class'] = 'form-control'

class ProductForm(StyleFormMixin, forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'
        # fields = (
        #     "name",
        #     "description",
        #     "image",
        #     "category",
        #     "price",
        #     "created_at",
        #     "updated_at",
        # ) казино, криптовалюта, крипта, биржа, дешево, бесплатно, обман, полиция, радар
    def clean(self):
        blacklist = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']

        cleaned_data = self.cleaned_data['name'] + self.cleaned_data['description']

        for b_word in blacklist:
            if b_word in cleaned_data:
                raise forms.ValidationError('Нельзя использовать слова из списка запрещенных (казино, криптовалюта, крипта, биржа, дешево, бесплатно, обман, полиция, радар)')

        else:
            return self.cleaned_data

class ContactForm(StyleFormMixin, forms.ModelForm):

    class Meta:
        model = Contact
        fields = (
            "name",
            "phone",
            "message",
        )

class VersionForm(StyleFormMixin, forms.ModelForm):

    class Meta:
        model = Version
        fields = "__all__"

        """    product, number, name, sign """