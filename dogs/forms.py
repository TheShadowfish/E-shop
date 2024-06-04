from django.forms import ModelForm, BooleanField

from dogs.models import Dog, Parent

class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, BooleanField):
                field.widget.attrs['class'] = 'form-check-input'
            else:
                field.widget.attrs['class'] = 'form-control'


class DogForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Dog
        fields = "__all__"
        exclude = ("count_views",)
        # fields = ("name", "breed", "photo", "date_born",)

class ParentForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Parent
        fields = '__all__'
