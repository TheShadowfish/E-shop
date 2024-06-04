from django.forms import ModelForm

from dogs.models import Dog, Parent


class DogForm(ModelForm):
    class Meta:
        model = Dog
        fields = "__all__"
        exclude = ("count_views",)
        # fields = ("name", "breed", "photo", "date_born",)

class ParentForm(ModelForm):
    class Meta:
        model = Parent
        fields = '__all__'
