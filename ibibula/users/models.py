from django.db import models
from django.contrib.auth.models import AbstractUser

from main.models import Services
from users.validators import validate_telegram

class User(AbstractUser):
    image = models.ImageField(upload_to='users_images', blank=True, null=True, verbose_name='Аватар')
    phone_number = models.CharField(max_length=10, verbose_name='Номер телефона')
    telegram = models.CharField(max_length=100, validators=[validate_telegram], verbose_name='Телеграм')
    email = models.EmailField(blank=True, null=True, verbose_name='Электронная почта')

    class Meta:
        db_table = 'user'
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username

class Performer(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, verbose_name='Пользователь')
    services = models.ManyToManyField(to=Services, verbose_name='Услуги')

    class Meta:
        verbose_name = 'Исполнитель'
        verbose_name_plural = 'Исполнители'

    def __str__(self):
        return self.user.username

class Buyer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    performer = models.ManyToManyField(to=Performer, verbose_name='Исполнитель')
    services = models.ForeignKey(to=Services, on_delete=models.CASCADE, verbose_name='Услуги')

    class Meta:
        verbose_name = 'Покупатель'
        verbose_name_plural = 'Покупатели'

    def __str__(self):
        return self.user.username