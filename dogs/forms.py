from django.core.exceptions import ValidationError
from django.forms import ModelForm, BooleanField
from django.utils import timezone
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

    def clean_year_born(self):
        year_born = self.cleaned_data['year_born']
        current_year = timezone.now().year
        timedelta = current_year - year_born
        if timedelta >= 100:
            raise ValidationError("Собаки столько не живут. проверьте год рождения.")
        return year_born