from django.shortcuts import render
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


def contacts(request):
    number = len(Contact.objects.all())
    contacts_list = Contact.objects.all()[number-5: number+1]

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


