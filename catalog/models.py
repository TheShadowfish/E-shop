from django.db import models

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
    - Наименование
    - Описание
    - Изображение (превью)
    - Категория
    - Цена за покупку
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
        **NULLABLE, verbose_name="Дата создания", help_text="Укажите дату создания"
    )
    updated_at = models.DateField(
        **NULLABLE, verbose_name="Дата изменения", help_text="Укажите дату изменения"
    )


    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ["category", "name"]

    def __str__(self):
        return self.name