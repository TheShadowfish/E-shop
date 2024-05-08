from django.urls import path
from dogs.apps import DogsConfig
# from dogs.views import home, contacts

app_name = DogsConfig.name

urlpatterns = [
    # path('', home, name='home'),
    # path('contacts/', contacts, name='contacts'),
]
