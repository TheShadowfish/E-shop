# Generated by Django 4.2.2 on 2024-06-11 06:47

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("catalog", "0007_alter_contact_time"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="owner",
            field=models.ForeignKey(
                blank=True,
                help_text="Укажите создателя продукта",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to=settings.AUTH_USER_MODEL,
                verbose_name="Владелец",
            ),
        ),
        migrations.AlterField(
            model_name="contact",
            name="time",
            field=models.DateTimeField(
                blank=True,
                default=datetime.datetime(
                    2024, 6, 11, 6, 47, 53, 264532, tzinfo=datetime.timezone.utc
                ),
                help_text="Укажите дату создания",
                null=True,
                verbose_name="Дата создания",
            ),
        ),
    ]
