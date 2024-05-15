from django.shortcuts import render

from dogs.models import Dog


def dogs_list(request):
    dogs = Dog.objects.all()
    context = {
        "dogs": dogs,
    }
    return render(request, 'dogs/base.html', context)


def contacts(request):
    return render(request, 'dogs/base.html')