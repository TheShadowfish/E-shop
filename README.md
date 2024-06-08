Для работы проекта необходимо

python = "^3.10"
django = "^5.0.4"
psycopg2 = "^2.9.9"
ipython = "^8.24.0"
pillow = "^10.3.0"
pytils = "^0.4.1"
python-decouple = "^3.8"

python-decouple нужен для хранения личных данных 
(имя БД Postgress, 
password,
email,
email_password
)


# Задание 1 (+) реализовано
Продолжаем работать с проектом из предыдущего домашнего задания. Для модели продуктов реализуйте механизм CRUD, задействовав модуль 
django.forms
.

Условия для пользователей:

**могут** создавать новые продукты,

**не могут** создавать продукты с запрещенными словами в названии и описании.

Для исключения загрузки запрещенных продуктов реализуйте валидацию названия и описания продукта
таким образом, чтобы нельзя было в них добавлять слова: 

**казино, криптовалюта, крипта, биржа, дешево, бесплатно, обман, полиция, радар.**

Для настройки валидации внутри формы определите методы 

clean
 для полей (например, 
clean_name()
). При наличии запрещенных слов — выбрасывайте ошибку 
forms.ValidationError()
 с соответствующим сообщением. Если валидация проходит успешно, возвращайте 
cleaned_data
.

# Задание 2 (+) тяжко пошло...
Добавьте новую модель «Версия», которая должна содержать следующие поля:

- продукт,
- номер версии,
- название версии,
- признак текущей версии.

- При наличии активной версии реализуйте вывод в список продуктов информации об активной версии.

Признак текущей версии — булево поле, является ли версия для продукта текущей для отображения на сайте или нет.

Для отображения активной версии расширьте метод 
get_context_data()
 контроллера списка продуктов, получите данные о версиях продукта и выберите текущую (активную) версию для продукта.

# Задание 3 (+)
Добавьте реализацию работы с формами для версий продукта.

Примечание

Все созданные формы нужно стилизовать так, чтобы они были в единой стилистике оформления всей платформы. Для этого можно воспользоваться методом 
__init__
 либо самостоятельно изучить пакет crispy-forms.

При стилизации формы методом 
__init__
 можно создать класс-миксин для сокращения дублирования кода.

Для стилизации булевого поля используйте специальный стиль — 
form-check-input
.

# Дополнительное задание
В один момент может быть только одна активная версия продукта, поэтому при изменении версий необходимо проверять, что пользователь в качестве активной версии указал только одну. В случае возникновения ошибки вернуть сообщение пользователю и попросить выбрать только одну активную версию.

Дополнительное задание, помеченное звездочкой, желательно, но не обязательно выполнять.