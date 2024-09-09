from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    email = models.EmailField(unique=True, null=False)
    username = models.CharField(max_length=100)
    bio = models.CharField(max_length=180)
    avatar = models.ImageField(upload_to='user/avatars/', null=True)
    phone_number = models.CharField(max_length=18, default='', verbose_name='Номер телефона пользователя')

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['username']

    class Meta:
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.username
