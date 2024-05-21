# Задание 1
Переведите имеющиеся контроллеры с FBV на CBV.

Не забудьте про контроллер контактов. Для его замены можно воспользоваться 
View
 или 
TemplateView
. Документацию можно найти тут.

# Задание 2
Создайте новую модель блоговой записи со следующими полями:

заголовок;
slug (реализовать через CharField);
содержимое;
превью (изображение);
дата создания;
признак публикации;
количество просмотров.
Для работы с блогом реализуйте CRUD для новой модели.

CRUD реализуйте на основе CBV (
ListView
, 
DetailView
, 
CreateView
, 
UpdateView
, 
DeleteView
) Соблюдайте нейминг шаблонов для CBV контроллеров - …_list.html, …_detail.html, …_form.html.

***Примечание***

Slug — человекопонятный URL, представляет собой набор символов, которые можно прочитать как связные слова или предложения в адресной строке и который служит уникальным идентификатором записи в рамках одной модели. Состоит из безопасных для обработки запроса символов:

0–9
a–z
 (обычно в нижнем регистре)
символ 
-
# Задание 3
Модифицируйте вывод и обработку запросов, добавив следующую логику на уровне контроллеров:

При открытии отдельной статьи увеличивать счетчик просмотров.
Для решения этой задачи можно воспользоваться переопределением метода 
get_object()
 в 
DetailView
.

Подсказка
Выводить в список статей только те, которые имеют положительный признак публикации.
Признак публикации — булево поле. Статья может быть опубликована или нет (
True
/
False
). Отфильтруйте статьи блога с помощью ORM-запроса.

При создании динамически формировать slug name для заголовка.
Для решения этой задачи можно воспользоваться переопределением метода 
form_valid()
 в 
CreateView
.

Подсказка
После успешного редактирования записи необходимо перенаправлять пользователя на просмотр этой статьи.
Для решения этой задачи можно воспользоваться переопределением метода 
get_success_url()
 в 
UpdateView
. Метод должен возращать объект 
reverse
 с параметрами 
args
.

# Дополнительное задание
Когда статья достигает 100 просмотров, отправлять себе на почту поздравление с достижением.

Примечание: для отправки писем рекомендуем использовать почтовый сервис «Яндекса».

Дополнительное задание, помеченное звездочкой, выполнять желательно, но не обязательно.