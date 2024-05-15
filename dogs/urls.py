from django.urls import path
from dogs.apps import DogsConfig
from dogs.views import dogs_list, contacts

app_name = DogsConfig.name

urlpatterns = [
    path('', dogs_list, name='dogs_list'),
    path('', contacts, name='contacts'),
]
