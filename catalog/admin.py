from django.contrib import admin

from django.contrib import admin
from catalog.models import Category, Product, Contact, Version

"""
Для категорий выведите **id** и **наименование** в список отображения, 
а для продуктов выведите в список **id**, **название**, **цену** и **категорию**.

При этом интерфейс вывода продуктов настройте так, 
чтобы можно было результат отображения фильтровать по категории, 
а также осуществлять поиск по названию и полю описания.
"""


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "price", "category")
    list_filter = ("category",)
    search_fields = ("name", "description")


@admin.register(Version)
class Product_versionAdmin(admin.ModelAdmin):
    list_display = ("id", "sign", "number", "name", "product")
    list_filter = ("number",)
    search_fields = ("sign", "product")


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")


@admin.register(Contact)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "phone", "message", "time")
