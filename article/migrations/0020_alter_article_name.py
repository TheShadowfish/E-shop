# Generated by Django 4.2.2 on 2024-06-23 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("article", "0019_alter_article_created_at"),
    ]

    operations = [
        migrations.AlterField(
            model_name="article",
            name="name",
            field=models.SlugField(
                help_text="Введите url статьи", max_length=100, verbose_name="url"
            ),
        ),
    ]
