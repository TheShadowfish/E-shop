from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from dogs.models import Dog

class DogListView(ListView):
    model = Dog

class DogDetailView(DetailView):
    model = Dog
    def qet_object(self, queryset = None):
        self.object = super().get_object(queryset)
        self.object.count_views += 1
        self.object.save()
        return self.object

class DogCreateView(CreateView):
    model= Dog
    fields = ("name", "breed", "photo", "date_born", )
    success_url = reverse_lazy('dogs:dogs_list')

class DogUpdateView(UpdateView):
    model = Dog
    fields = ("name", "breed", "photo", "date_born",)
    success_url = reverse_lazy('dogs:dogs_list')

    def get_success_url(self):
        return reverse('dogs:detail', args=[self.kwargs.get("pk")])

class DogDeleteView(DeleteView):
    model = Dog
    success_url = reverse_lazy('dogs:dogs_list')

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