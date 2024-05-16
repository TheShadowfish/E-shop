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
    # products_list = Product.objects.all()
    # product_list = products_list[per_page * (page - 1): per_page * page]

    len_product = len(Product.objects.all())
    if len_product % per_page != 0:
        page_count = [x+1 for x in range((len_product // per_page) + 1)]
    else:
        page_count = [x + 1 for x in range((len_product // per_page))]


    # page_count = [x+1 for x in range(len(Product.objects.all()) // per_page)]

    product_list = Product.objects.all()[per_page * (page - 1): per_page * page]




    context = {
        "product_list": product_list,
        "page": page,
        "per_page": per_page,
        "page_count": page_count
    }
    print(context)

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

        # print(f'Write contacts: {name}({phone}): {message}')
        #
        # parent_dir = os.path.dirname(os.path.abspath(os.path.dirname(os.path.abspath(__file__))))
        # logger = Logger(os.path.join(parent_dir, 'data/contacts.txt'))

        info = {'time': (datetime.now()).strftime('%Y-%m-%dT%H:%M:%S.%f'),
                'name': name, 'phone': phone, 'message': message
                }

        # print(item)

        # Contact.objects.append(Contact(**info))
        # students_for_create.append(Student(**student_item))

        # logger(info)
        Contact.objects.create(**info)

    return render(request, 'catalog/contacts.html', context)

# class Logger:
#     def __init__(self, filepath):
#         self.filepath = filepath
#
#     def __call__(self, info: dict):
#         # dict_user = {key: value for (key, value) in info.items()}
#         # dict_user['time'] = (datetime.now()).strftime('%Y-%m-%dT%H:%M:%S.%f')
#
#         try:
#             with open(self.filepath, "at") as write_file:
#                 write_file.write(str(info))
#                 write_file.write('\n')
#         except OSError as e:
#             print(f"Something went wrong. I can't write \"{self.filepath}\", {str(e)}")
