from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from d_users.forms import UserRegisterForm
from d_users.models import D_user


class UserCreateView(CreateView):
    model= D_user
    form_class = UserRegisterForm
    success_url = reverse_lazy('d_users:login')
