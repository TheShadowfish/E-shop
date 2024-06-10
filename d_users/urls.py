from django.contrib.auth.views import LoginView
from django.urls import path

from d_users.apps import DUsersConfig


app_name = DUsersConfig.name

urlpatterns = [
    path('login/', LoginView.as_view(template_name = "login.html")),

]
