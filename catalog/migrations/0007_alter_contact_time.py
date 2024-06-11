# Generated by Django 4.2.2 on 2024-06-11 04:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0006_alter_contact_time"),
    ]

    operations = [
        migrations.AlterField(
            model_name="contact",
            name="time",
            field=models.DateTimeField(
                blank=True,
                default=datetime.datetime(
                    2024, 6, 11, 4, 20, 47, 160312, tzinfo=datetime.timezone.utc
                ),
                help_text="Укажите дату создания",
                null=True,
                verbose_name="Дата создания",
            ),
        ),
    ]