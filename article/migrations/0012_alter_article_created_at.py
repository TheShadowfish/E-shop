# Generated by Django 4.2 on 2024-06-10 07:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("article", "0011_alter_article_created_at"),
    ]

    operations = [
        migrations.AlterField(
            model_name="article",
            name="created_at",
            field=models.DateField(
                blank=True,
                default=datetime.datetime(
                    2024, 6, 10, 7, 22, 13, 80994, tzinfo=datetime.timezone.utc
                ),
                help_text="Укажите дату создания",
                null=True,
                verbose_name="Дата создания",
            ),
        ),
    ]
