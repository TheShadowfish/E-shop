from django.shortcuts import render, get_object_or_404
from datetime import datetime
import os

from django.urls import reverse_lazy

from catalog.forms import ProductForm
from catalog.models import Category, Product, Contact

from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    TemplateView,
)


class ProductListView(ListView):
    model = Product
    queryset = model.objects.all()  # Default: Model.objects.all()

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)

        if self.request.method == 'POST':
            context_data['formset'] = TagFormSet(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = TagFormSet(instance=self.object)

        return context_data



"""
# Задание 2


- При наличии активной версии реализуйте вывод в список продуктов информации об активной версии.
Для отображения активной версии расширьте метод 
get_context_data()
 контроллера списка продуктов, получите данные о версиях продукта и выберите текущую (активную) версию для продукта.
 def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        TagFormSet = inlineformset_factory(Article, Tag, form=TagForm, extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = TagFormSet(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = TagFormSet( instance=self.object)

        return context_data

    def form_valid(self, form):
        formset = self.get_context_data()['formset']
        self.object = form.save()
        if formset.is_valid():
            formset.instance = self.object
            formset.save()

        return super().form_valid(form)

"""

class ProductPaginate2ListView(ListView):
    model = Product
    paginate_by = 2
    queryset = model.objects.all()  # Default: Model.objects.all()


class ProductPaginate3ListView(ListView):
    model = Product
    paginate_by = 3
    queryset = model.objects.all()  # Default: Model.objects.all()


class ProductDetailView(DetailView):
    model = Product


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("catalog:home")
    # """Product
    # - Наименование name
    # - Описание description
    # - Изображение (превью) image
    # - Категория category
    # - Цена за покупку price
    # - Дата создания (записи в БД) created_at
    # - Дата последнего изменения (записи в БД) updated_at"""
    #
    # model = Product
    # fields = (
    #     "name",
    #     "description",
    #     "image",
    #     "category",
    #     "price",
    #     "created_at",
    #     "updated_at",
    # )
    # success_url = reverse_lazy("catalog:home")


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("catalog:home")
    # model = Product
    # fields = (
    #     "name",
    #     "description",
    #     "image",
    #     "category",
    #     "price",
    #     "created_at",
    #     "updated_at",
    # )
    # success_url = reverse_lazy("catalog:home")


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy("catalog:home")


class ContactsPageViews(CreateView):
    model = Contact
    fields = (
        "name",
        "phone",
        "message",
    )
    success_url = reverse_lazy("catalog:contacts")
    template_name = "catalog/contacts.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        number = len(Contact.objects.all())
        if number > 5:
            context["latest_contacts"] = Contact.objects.all()[number - 5 : number + 1]
        else:
            context["latest_contacts"] = Contact.objects.all()

        return context


def contacts(request):
    number = len(Contact.objects.all())
    if number > 5:
        contacts_list = Contact.objects.all()[number - 5 : number + 1]
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
