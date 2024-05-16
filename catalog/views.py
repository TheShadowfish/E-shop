from django.shortcuts import render, get_object_or_404
from datetime import datetime
import os
from catalog.models import Category, Product, Contact


def home(request):
    products_list = Product.objects.all()
    categoryies_list = Category.objects.all()
    # Product.objects.all().delete()
    # Category.objects.all().delete()
    #
    #
    context = {
        'object_list': products_list,
        'title': 'Каталог'
    }

    return render(request, 'catalog/home.html', context)

def catalog(request, page, per_page):

    len_product = len(Product.objects.all())
    if len_product % per_page != 0:
        page_count = [x+1 for x in range((len_product // per_page) + 1)]
    else:
        page_count = [x + 1 for x in range((len_product // per_page))]

    product_list = Product.objects.all()[per_page * (page - 1): per_page * page]


    context = {
        "product_list": product_list,
        "page": page,
        "per_page": per_page,
        "page_count": page_count
    }


    return render(request, 'catalog/per_page.html', context)


def product_detail(request, pk, page=None, per_page=None):
    _object = get_object_or_404(Product, pk=pk)
    context = {
        "object": _object,
        "pagination": bool(per_page),
        "per_page": per_page,
        "page": page
    }

    return render(request, 'catalog/product_detail.html', context)


def contacts(request):
    number = len(Contact.objects.all())
    if number > 5:
        contacts_list = Contact.objects.all()[number - 5: number + 1]
    else:
        contacts_list = Contact.objects.all()

    context = {
        'object_list': contacts_list,
        'title': 'Контакты'
    }

    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')


        info = {'time': (datetime.now()).strftime('%Y-%m-%dT%H:%M:%S.%f'),
                'name': name, 'phone': phone, 'message': message
                }

        Contact.objects.create(**info)

    return render(request, 'catalog/contacts.html', context)


def create(request):
    """
       Product
       - Наименование name
       - Описание description
       - Изображение (превью) image
       - Категория category
       - Цена за покупку price
       - Дата создания (записи в БД) created_at
       - Дата последнего изменения (записи в БД) updated_at
       """



    number = len(Product.objects.all())
    if number > 5:
        products_list = Product.objects.all()[number - 5: number + 1]
    else:
        products_list = Product.objects.all()


    category_list = Category.objects.all()



    context = {
        'object_list': products_list,
        'category_list': category_list,
        'title': 'Добавить продукт',
    }

    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        price = request.POST.get('price')
        category = request.POST.get('category')
        image = request.POST.get('image')

        time_of_creation = (datetime.now()).strftime('%Y-%m-%d')



        info = {'created_at': time_of_creation,
                'updated_at': time_of_creation,
                'name': name, 'price': price, 'description': description,
                'category': Category.objects.get(id=category), 'image': image
                }

        print(info)
        Product.objects.create(**info)

        # product_for_create.append(
        #     Product(
        #         pk=item["pk"],
        #         name=item["fields"]["name"],
        #         description=item["fields"]["description"],
        #         image=item["fields"]["image"],
        #         category=Category.objects.get(id=item["fields"]["category"]),
        #         price=item["fields"]["price"],
        #         created_at=item["fields"]["created_at"],
        #         updated_at=item["fields"]["updated_at"],
        #     )
        # )

        # Product.objects.bulk_create(product_for_create)

    return render(request, 'catalog/create_product.html', context)
