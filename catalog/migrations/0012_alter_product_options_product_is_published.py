# Generated by Django 4.2.2 on 2024-06-17 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0011_alter_contact_time"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="product",
            options={
                "ordering": ["category", "name"],
                "permissions": [
                    ("can_change_is_published_field", "Can change sign of publication"),
                    ("can_edit_description", "Can edit description"),
                    ("can_edit_category", "Can edit category"),
                ],
                "verbose_name": "Продукт",
                "verbose_name_plural": "Продукты",
            },
        ),
        migrations.AddField(
            model_name="product",
            name="is_published",
            field=models.BooleanField(
                default=False,
                help_text="Укажите признак публикации",
                verbose_name="Признак публикации",
            ),
        ),
    ]
