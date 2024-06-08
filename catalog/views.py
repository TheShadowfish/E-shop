from django.shortcuts import render
from datetime import datetime

from django.urls import reverse_lazy

from catalog.forms import ProductForm, ContactForm, VersionForm
from catalog.models import Product, Contact, Version

from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)


class GetContextMixin:
    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['version'] = Version.objects.all()
        return context_data


class ProductListView(GetContextMixin, ListView):
    model = Product


class Product2ListView(GetContextMixin, ListView):
    model = Product
    paginate_by = 2
    # queryset = model.objects.all()  # Default: Model.objects.all()


class Product3ListView(GetContextMixin, ListView):
    model = Product
    paginate_by = 3
    # queryset = model.objects.all()  # Default: Model.objects.all()


class ProductDetailView(DetailView):
    model = Product


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("catalog:home")


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("catalog:home")


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy("catalog:home")


class ContactsPageViews(CreateView):
    model = Contact
    form_class = ContactForm
    # fields = (
    #     "name",
    #     "phone",
    #     "message",
    # )
    success_url = reverse_lazy("catalog:contacts")
    template_name = "catalog/contacts.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        number = len(Contact.objects.all())
        if number > 5:
            context["latest_contacts"] = Contact.objects.all()[number - 5: number + 1]
        else:
            context["latest_contacts"] = Contact.objects.all()

        return context


def contacts(request):
    number = len(Contact.objects.all())
    if number > 5:
        contacts_list = Contact.objects.all()[number - 5: number + 1]
    else:
        contacts_list = Contact.objects.all()

    context = {"object_list": contacts_list, "title": "Контакты"}

    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        message = request.POST.get("message")

        info = {
            "time": (datetime.now()).strftime("%Y-%m-%dT%H:%M:%S.%f"),
            "name": name,
            "phone": phone,
            "message": message,
        }

        Contact.objects.create(**info)

    return render(request, "catalog/contacts.html", context)


class VersionListView(ListView):
    model = Version


class VersionDetailView(DetailView):
    model = Version


class VersionCreateView(CreateView):
    model = Version
    form_class = VersionForm
    success_url = reverse_lazy("catalog:versions")


class VersionUpdateView(UpdateView):
    model = Version
    form_class = VersionForm
    success_url = reverse_lazy("catalog:versions")


class VersionDeleteView(DeleteView):
    model = Version
    success_url = reverse_lazy("catalog:versions")
