from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render

from django.shortcuts import render, get_object_or_404
from datetime import datetime
import os

from django.urls import reverse_lazy, reverse
from pytils.translit import slugify

from article.forms import ArticleForm
from article.functions.utils import send_email

from article.models import Article

from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
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


class ArticleCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):

    model = Article

    form_class = ArticleForm
    permission_required = "article.add_article"

    success_url = reverse_lazy("article:blog")

    login_url = "users:login"
    redirect_field_name = "login"

    def form_valid(self, form):
        if form.is_valid():
            new_article = form.save()
            new_article.slug = slugify(new_article.name)
            new_article.save()
        return super().form_valid(form)


class ArticleUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Article
    form_class = ArticleForm
    permission_required = "article.change_article"

    # success_url = reverse_lazy('article:blog')

    login_url = "users:login"
    redirect_field_name = "login"

    def form_valid(self, form):
        if form.is_valid():
            new_article = form.save()
            new_article.slug = slugify(new_article.name)
            new_article.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("article:article_detail", args=[self.kwargs.get("pk")])


class ArticleDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Article
    success_url = reverse_lazy("article:blog")
    permission_required = "article.delete_article"

    login_url = "users:login"
    redirect_field_name = "login"
