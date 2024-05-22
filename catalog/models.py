from django.db import models
from datetime import datetime
from django.utils import timezone
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
        verbose_name="Описание категории", help_text="Введите описание категории товаров", **NULLABLE
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
        max_length=100, verbose_name="Наименование", help_text="Введите наименование продукта"
    )
    description = models.TextField(
        verbose_name="Описание продукта", help_text="Введите описание продукта", **NULLABLE
    )
    image = models.ImageField(
        upload_to="product/photo",
        verbose_name="Изображение",
        help_text="Загрузите изображение продукта",
        **NULLABLE
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        verbose_name="Категории",
        help_text="Введите категорию продукта",
        **NULLABLE,
        related_name="categories"
    )

    price = models.IntegerField(verbose_name="Цена", help_text="Введите цену продукта")

    created_at = models.DateField(
        **NULLABLE, verbose_name="Дата создания", help_text="Укажите дату создания", default=timezone.now()
    )
    updated_at = models.DateField(
        **NULLABLE, verbose_name="Дата изменения", help_text="Укажите дату изменения", default=timezone.now()
    )

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ["category", "name"]

    def __str__(self):
        return self.name


class Contact(models.Model):
    """
    info = {'time': (datetime.now()).strftime('%Y-%m-%dT%H:%M:%S.%f'),
            'name': name, 'phone': phone, 'message': message
            }
            """
    """
    Contact
    - Имя name
    - Телефон phone
    - Сообщение message
    - Время отправки time
    """
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
        verbose_name="Сообщение",
        help_text="Введите сообщение контакта", **NULLABLE
    )
    time = models.DateTimeField(
        **NULLABLE, verbose_name="Дата создания", help_text="Укажите дату создания", default=timezone.now()
    )

    class Meta:
        verbose_name = "Контакт"
        verbose_name_plural = "Контакты"

    def __str__(self):
        return f"{self.name} - {self.phone}"
