from django.shortcuts import render

from django.shortcuts import render, get_object_or_404
from datetime import datetime
import os

from django.urls import reverse_lazy

from article.models import Article

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView


class ArticleListView(ListView):
    model = Article
    # paginate_by = 3
    # queryset = model.objects.all()  # Default: Model.objects.all()


class ArticleDetailView(DetailView):
    model = Article


class ArticleCreateView(CreateView):

    model = Article
    fields = ("name", "slug", "body", "image", "created_at", "is_published", "views_count",)

    success_url = reverse_lazy('article:blog')


class ArticleUpdateView(UpdateView):
    model = Article
    fields = ("name", "slug", "body", "image", "created_at", "is_published", "views_count",)
    success_url = reverse_lazy('article:blog')


class ArticleDeleteView(DeleteView):
    model = Article
    success_url = reverse_lazy('article:blog')

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
