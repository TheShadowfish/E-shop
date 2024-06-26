# Generated by Django 5.0.4 on 2024-06-05 12:59

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0003_alter_contact_message_alter_contact_time_version"),
    ]

    operations = [
        migrations.AlterField(
            model_name="contact",
            name="time",
            field=models.DateTimeField(
                blank=True,
                default=datetime.datetime(
                    2024, 6, 5, 12, 59, 29, 948838, tzinfo=datetime.timezone.utc
                ),
                help_text="Укажите дату создания",
                null=True,
                verbose_name="Дата создания",
            ),
        ),
        migrations.AlterField(
            model_name="version",
            name="product",
            field=models.ForeignKey(
                help_text="название продукта",
                on_delete=django.db.models.deletion.CASCADE,
                related_name="product",
                to="catalog.product",
                verbose_name="продукт",
            ),
        ),
    ]
