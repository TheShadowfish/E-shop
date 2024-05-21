from django.urls import path
from dogs.apps import DogsConfig
from dogs.views import contacts, DogListView, DogDetailView, DogCreateView, DogUpdateView, DogDeleteView

app_name = DogsConfig.name

urlpatterns = [
    path('', DogListView.as_view(), name='dogs_list'),
    path('dogs/<int:pk>/', DogDetailView.as_view(), name='dogs_detail'),
    path('contacts/', contacts, name='contacts'),
    path('dogs/create/', DogCreateView.as_view(), name='dogs_create'),
    path('dogs/<int:pk>/update', DogUpdateView.as_view(), name='dogs_update'),
    path('dogs/<int:pk>/delete', DogDeleteView.as_view(), name='dogs_delete')
]
