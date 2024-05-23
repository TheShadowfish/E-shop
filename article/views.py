from django.shortcuts import render

from django.shortcuts import render, get_object_or_404
from datetime import datetime
import os

from django.urls import reverse_lazy, reverse
from pytils.translit import slugify
from article.functions.utils import send_email

from article.models import Article

from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)


class ArticleListView(ListView):
    model = Article

    # paginate_by = 3
    # queryset = model.objects.all()  # Default: Model.objects.all()
    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_published=True)
        return queryset


class ArticleDetailView(DetailView):
    model = Article

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()

        if self.object.views_count == 100:
            send_email(self.object)

        return self.object


class ArticleCreateView(CreateView):

    model = Article
    fields = (
        "name",
        "body",
        "image",
        "created_at",
        "is_published",
        "views_count",
    )

    success_url = reverse_lazy("article:blog")

    def form_valid(self, form):
        if form.is_valid():
            new_article = form.save()
            new_article.slug = slugify(new_article.name)
            new_article.save()
        return super().form_valid(form)


class ArticleUpdateView(UpdateView):
    model = Article
    fields = (
        "name",
        "body",
        "image",
        "created_at",
        "is_published",
        "views_count",
    )
    # success_url = reverse_lazy('article:blog')

    def form_valid(self, form):
        if form.is_valid():
            new_article = form.save()
            new_article.slug = slugify(new_article.name)
            new_article.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("article:article_detail", args=[self.kwargs.get("pk")])


class ArticleDeleteView(DeleteView):
    model = Article
    success_url = reverse_lazy("article:blog")


#
# class ContactsPageViews(CreateView):
#     model = Contact
#     fields = ("name", "phone", "message",)
#     success_url = reverse_lazy('catalog:contacts')
#     template_name = "catalog/contacts.html"
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#
#         number = len(Contact.objects.all())
#         if number > 5:
#             context["latest_contacts"] = Contact.objects.all()[number - 5: number + 1]
#         else:
#             context["latest_contacts"] = Contact.objects.all()
#
#         return context
#
#
# def contacts(request):
#     number = len(Contact.objects.all())
#     if number > 5:
#         contacts_list = Contact.objects.all()[number - 5: number + 1]
#     else:
#         contacts_list = Contact.objects.all()
#
#     context = {
#         'object_list': contacts_list,
#         'title': 'Контакты'
#     }
#
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         phone = request.POST.get('phone')
#         message = request.POST.get('message')
#
#         info = {'time': (datetime.now()).strftime('%Y-%m-%dT%H:%M:%S.%f'),
#                 'name': name, 'phone': phone, 'message': message
#                 }
#
#         Contact.objects.create(**info)
#
#     return render(request, 'catalog/contacts.html', context)
