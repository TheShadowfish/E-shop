import json
import os

from django.core.management import BaseCommand
from catalog.models import Category, Product


class Command(BaseCommand):

    def handle(self, *args, **options):

        # Зачистка базы данных от старых данных
        Product.objects.all().delete()
        Category.objects.all().delete()

        product_for_create = []
        category_for_create = []

        # Обходим все значения категорий из фиктсуры для получения информации об одном объекте
        for item in Command.json_read_categories(
            os.path.join("data", "catalog_data_categories.json")
        ):
            # print(item)

            category_for_create.append(
                Category(
                    pk=item["pk"],
                    name=item["fields"]["name"],
                    description=item["fields"]["description"],
                )
            )
        Category.objects.bulk_create(category_for_create)

        for item in Command.json_read_products(
            os.path.join("data", "catalog_data_products.json")
        ):
            # print(item)

            product_for_create.append(
                Product(
                    pk=item["pk"],
                    name=item["fields"]["name"],
                    image=item["fields"]["image"],
                    category=Category.objects.get(id=item["fields"]["category"]),
                    price=item["fields"]["price"],
                    created_at=item["fields"]["created_at"],
                    updated_at=item["fields"]["updated_at"],
                )
            )

        Product.objects.bulk_create(product_for_create)

    @staticmethod
    def json_read_categories(filepath):
        """
        Здесь мы получаем данные из фикстуры с категориями
        """
        if not os.path.exists(filepath):
            raise FileNotFoundError(f"file {filepath} not found!")

        with open(filepath, "rt") as read_file:
            data_json = json.load(read_file)

        return data_json

    @staticmethod
    def json_read_products(filepath):
        """
        Здесь мы получаем данные из фикстуры с продуктами
        """
        if not os.path.exists(filepath):
            raise FileNotFoundError(f"file {filepath} not found!")

        with open(filepath, "rt") as read_file:
            data_json = json.load(read_file)

        return data_json
