from django.db import models
from datetime import datetime
from django.utils import timezone

from users.models import User

NULLABLE = {"blank": True, "null": True}


class Category(models.Model):
    """
    Category
    - Наименование
    - Описание
    """

    name = models.CharField(
        max_length=100,
        verbose_name="Наименование категории",
        help_text="Введите наименование категории",
    )
    description = models.TextField(
        verbose_name="Описание категории",
        help_text="Введите описание категории товаров",
        **NULLABLE,
    )

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name


class Product(models.Model):
    """
    Product
    - Наименование name
    - Описание description
    - Изображение (превью) image
    - Категория category
    - Цена за покупку price
    - Дата создания (записи в БД) created_at
    - Дата последнего изменения (записи в БД) updated_at
    """

    name = models.CharField(
        max_length=100,
        verbose_name="Наименование",
        help_text="Введите наименование продукта",
    )
    description = models.TextField(
        verbose_name="Описание продукта",
        help_text="Введите описание продукта",
        **NULLABLE,
    )
    image = models.ImageField(
        upload_to="product/photo",
        verbose_name="Изображение",
        help_text="Загрузите изображение продукта",
        **NULLABLE,
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        verbose_name="Категории",
        help_text="Введите категорию продукта",
        **NULLABLE,
        related_name="categories",
    )

    price = models.IntegerField(verbose_name="Цена", help_text="Введите цену продукта")

    created_at = models.DateField(
        **NULLABLE,
        verbose_name="Дата создания",
        help_text="Укажите дату создания",
        auto_now_add=True,
    )
    updated_at = models.DateField(
        **NULLABLE,
        verbose_name="Дата изменения",
        help_text="Укажите дату изменения",
        auto_now=True,
    )
    owner = models.ForeignKey(
        User,
        verbose_name="Владелец",
        help_text="Укажите создателя продукта",
        **NULLABLE,
        on_delete=models.SET_NULL,
    )

    is_published = models.BooleanField(
        verbose_name="Признак публикации",
        help_text="Укажите признак публикации",
        default=False,
    )

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ["category", "name"]
        permissions = [
            ("can_change_is_published_field", "Can change sign of publication"),
            ("can_edit_description", "Can edit description"),
            ("can_edit_category", "Can edit category"),
        ]

    def __str__(self):
        return self.name


class Version(models.Model):

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        verbose_name="продукт",
        help_text="название продукта",
        related_name="product",
    )
    number = models.PositiveIntegerField(
        verbose_name="Номер версии",
        help_text="укажите номер версии",
    )
    name = models.CharField(
        max_length=100,
        verbose_name="Название версии",
        help_text="Введите название версии",
    )
    sign = models.BooleanField(verbose_name="Признак текущей версии")

    class Meta:
        verbose_name = "Версия"
        verbose_name_plural = "Версии"
        ordering = ["number", "name"]

    def __str__(self):
        return f"{self.number}-{self.name}:{self.sign}"


class Contact(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name="Имя контакта",
        help_text="Введите имя контакта",
    )
    phone = models.CharField(
        max_length=20,
        verbose_name="Телефон контакта",
        help_text="Введите телефон контакта",
    )
    message = models.TextField(
        verbose_name="Сообщение", help_text="Введите сообщение контакта", **NULLABLE
    )
    time = models.DateTimeField(
        **NULLABLE,
        verbose_name="Дата создания",
        help_text="Укажите дату создания",
        auto_now_add=True,
    )

    class Meta:
        verbose_name = "Контакт"
        verbose_name_plural = "Контакты"

    def __str__(self):
        return f"{self.name} - {self.phone}"
