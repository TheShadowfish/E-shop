from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from dogs.models import Dog

class DogListView(ListView):
    model = Dog

class DogDetailView(DetailView):
    model = Dog

class DogCreateView(CreateView):
    model= Dog
    fields = ("name", "breed", "photo", "date_born", )
    success_url = reverse_lazy('dogs:dog_list')
# def dogs_list(request):
#
#     dogs = Dog.objects.all()
#     context = {
#         "dogs": dogs,
#     }
#     return render(request, 'dogs/dogs_list.html', context)

#
# def dogs_detail(request, pk):
#
#     # dog = Dog.objects.get(pk=pk)
#     dog = get_object_or_404(Dog, pk=pk)
#     context = {
#         "dog": dog,
#     }
#
#     return render(request, 'dogs/dogs_detail.html', context)


def contacts(request):

    dogs = Dog.objects.all()
    context = {
        "object_list": dogs,
    }

    return render(request, 'dogs/contacts.html', context)