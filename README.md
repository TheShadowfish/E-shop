# Задание 1 (вроде как всё относительно прилично работает)
Переведите имеющиеся контроллеры с FBV на CBV.

Не забудьте про контроллер контактов. 

Документацию можно найти **в интернете на английском и еще надо умудриться её понять за ограниченное время**.


# Задание 2 (+)
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
- ListView, 
- DetailView, 
- CreateView, 
- UpdateView, 
-DeleteView
) 

Соблюдайте нейминг шаблонов для CBV контроллеров - …_list.html, …_detail.html, …_form.html.


# Задание 3 (+)
Модифицируйте вывод и обработку запросов, добавив следующую логику на уровне контроллеров:

При открытии отдельной статьи увеличивать счетчик просмотров. (+)

Выводить в список статей только те, которые имеют положительный признак публикации. (+)

При создании динамически формировать slug name для заголовка.(+)

После успешного редактирования записи необходимо перенаправлять пользователя на просмотр этой статьи. (+)


# Дополнительное задание
Когда статья достигает 100 просмотров, отправлять себе на почту поздравление с достижением.

Примечание: для отправки писем рекомендуем использовать почтовый сервис «Яндекса».
(да как это сделать-то? Что за библиотеку импортировать? 

Яндекс к почтовой программе-то не подключается без двухфакторной авторизации, как вообще это делать?)

Дополнительное задание, помеченное звездочкой, выполнять желательно, но не обязательно.