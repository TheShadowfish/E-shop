# Generated by Django 5.0.4 on 2024-06-03 19:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("article", "0003_alter_article_created_at_tag"),
    ]

    operations = [
        migrations.AlterField(
            model_name="article",
            name="created_at",
            field=models.DateField(
                blank=True,
                default=datetime.datetime(
                    2024, 6, 3, 19, 43, 11, 449046, tzinfo=datetime.timezone.utc
                ),
                help_text="Укажите дату создания",
                null=True,
                verbose_name="Дата создания",
            ),
        ),
        migrations.AlterField(
            model_name="article",
            name="name",
            field=models.CharField(
                help_text="Введите заголовок статьи",
                max_length=100,
                unique=True,
                verbose_name="Заголовок",
            ),
        ),
    ]
