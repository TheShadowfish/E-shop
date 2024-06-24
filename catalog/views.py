from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.cache import cache
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, get_object_or_404
from datetime import datetime

from django.urls import reverse_lazy

from catalog.forms import ProductForm, ContactForm, VersionForm, ProductModeratorForm
from catalog.models import Category, Product, Contact, Version

from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from catalog.services import get_cached_versions_for_products, get_cached_category, get_cached_products
from config import settings


class GetContextMixin:
    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)

        context_data["version"] = get_cached_versions_for_products()
        context_data['category_list'] = get_cached_category()
        # пагинация с этим не работает, а так кешируется конечно
        # context_data["object_list"] = get_cached_products()
        return context_data


class ProductListView(ListView):
    model = Product

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)

        context_data["version"] = get_cached_versions_for_products()
        # пагинация с этим не работает, а так кешируется конечно
        context_data["object_list"] = get_cached_products()
        context_data['category_list'] = get_cached_category()
        return context_data


class ProductListViewCategory(GetContextMixin, ListView):
    model = Product

    def get_queryset(self):
        self.category = get_object_or_404(Category, name=self.kwargs['name'])
        return Product.objects.filter(category_id=self.category)

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)

        context_data["version"] = get_cached_versions_for_products()
        # пагинация с этим не работает, а так кешируется конечно
        # context_data["object_list"] = get_cached_products()
        context_data['category_list'] = [self.category, ]
        return context_data


class Product2ListView(GetContextMixin, ListView):
    model = Product
    paginate_by = 2
    # queryset = model.objects.all()  # Default: Model.objects.all()


class Product3ListView(GetContextMixin, ListView):
    model = Product
    paginate_by = 3
    # queryset = model.objects.all()  # Default: Model.objects.all()


class ProductDetailView(GetContextMixin, DetailView):
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['mailing_list'] = Mailing.objects.all()
        context['category_list'] = get_cached_category()
        return context


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("catalog:home")

    login_url = "users:login"
    redirect_field_name = "login"

    def form_valid(self, form):
        product = form.save()
        user = self.request.user
        product.owner = user
        product.save()
        get_cached_products(recached=True)

        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("catalog:home")

    login_url = "users:login"
    redirect_field_name = "login"

    def get_form_class(self):
        user = self.request.user
        if user == self.object.owner:
            return ProductForm
        if (
                user.has_perm("catalog.can_change_is_published_field")
                and user.has_perm("catalog.can_edit_description")
                and user.has_perm("catalog.can_edit_category")
        ):
            return ProductModeratorForm
        raise PermissionDenied

    def form_valid(self, form):

        get_cached_products(recached=True)
        return super().form_valid(form)


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy("catalog:home")

    login_url = "users:login"
    redirect_field_name = "login"

    def form_valid(self, form):
        get_cached_products(recached=True)
        return super().form_valid(form)


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


@login_required
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


class CategoryListView(ListView):
    model = Category

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['mailing_list'] = Mailing.objects.all()
        context['category_list'] = get_cached_category()
        return context


class VersionDetailView(DetailView):
    model = Version


class VersionCreateView(LoginRequiredMixin, CreateView):
    model = Version
    form_class = VersionForm
    success_url = reverse_lazy("catalog:versions")

    login_url = "users:login"
    redirect_field_name = "login"

    def form_valid(self, form):
        product = form.save()
        user = self.request.user
        product.owner = user
        product.save()
        get_cached_versions_for_products(recached=True)
        return super().form_valid(form)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class VersionUpdateView(LoginRequiredMixin, UpdateView):
    model = Version
    form_class = VersionForm
    success_url = reverse_lazy("catalog:versions")

    login_url = "users:login"
    redirect_field_name = "login"

    def get_form_class(self):
        user = self.request.user
        version = self.version
        if user == version.product.owner:
            return ProductForm
        raise PermissionDenied

    def form_valid(self, form):
        get_cached_versions_for_products(recached=True)
        return super().form_valid(form)


class VersionDeleteView(LoginRequiredMixin, DeleteView):
    model = Version
    success_url = reverse_lazy("catalog:versions")

    login_url = "users:login"
    redirect_field_name = "login"

    def get_form_class(self):
        user = self.request.user
        version = self.version
        if user == version.product.owner:
            return ProductForm
        raise PermissionDenied

    def form_valid(self, form):
        get_cached_versions_for_products(recached=True)
        return super().form_valid(form)
