from django import forms
from catalog.models import Product, Contact


class ProductForm(forms.ModelForm):

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

class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = (
            "name",
            "phone",
            "message",
        )
