from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class D_user(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='Email')
    phone = models.CharField(max_length=35, verbose_name='телефон', **NULLABLE, help_text='введите номер телефона')
    tg_name = models.CharField(max_length=50, verbose_name='Ник телеграм', **NULLABLE, help_text='Введите ник телеграм')
    avatar = models.ImageField(upload_to='d_users/avatars', verbose_name='Аватар', **NULLABLE, help_text='Загрузите свой аватар')

    token = models.CharField(max_length=100, verbose_name='Token', **NULLABLE)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []


    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.email