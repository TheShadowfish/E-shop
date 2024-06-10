from django.contrib.auth.forms import UserCreationForm

from d_users.models import D_user
from dogs.forms import StyleFormMixin


class UserRegisterForm(StyleFormMixin, UserCreationForm):
    class Meta:
        model = D_user
        fields = ("email", "password1", "password2",)
