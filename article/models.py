from django.db import models
from django.utils import timezone

NULLABLE = {"blank": True, "null": True}


class Article(models.Model):
    """
    заголовок; title
    slug (реализовать через CharField);
    содержимое; body
    превью (изображение); image
    дата создания;
    признак публикации;
    количество просмотров.
    """
    name = models.CharField(
        max_length=100, verbose_name="Заголовок", help_text="Введите заголовок статьи"
    )
    slug = models.CharField(max_length=150, verbose_name='slug', help_text="slug", **NULLABLE)

    body = models.TextField(
        verbose_name="Содержимое статьи", help_text="Введите содержимое статьи"
    )
    image = models.ImageField(
        upload_to="blog/photo",
        verbose_name="Превью",
        help_text="Загрузите превью статьи",
        **NULLABLE
    )
    created_at = models.DateField(
        **NULLABLE, verbose_name="Дата создания", help_text="Укажите дату создания", default=timezone.now()
    )
    is_published = models.BooleanField(verbose_name="Признак публикации", help_text="Укажите признак публикации",
                                       default=True)

    views_count = models.PositiveIntegerField(verbose_name="Количество просмотров",
                                              help_text="Укажите количество просмотров", default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Запись в блоге"
        verbose_name_plural = "Записи в блоге"
