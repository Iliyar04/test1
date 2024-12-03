
# Create your models here.

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class CustomUser(AbstractUser):

    patronymic = models.CharField(max_length=150, blank=True, null=True)  # Отчество
    photo = models.ImageField(upload_to='user_photos/', blank=True, null=True, verbose_name='Фото')  # Поле для фото
    age = models.PositiveIntegerField(blank=True, null=True, verbose_name='Возраст')
    about = models.TextField(blank=True, null=True, verbose_name='О себе')

    def __str__(self):
        return self.username


from django.db import models
from django.contrib.auth.models import User


from django.db import models
from django.conf import settings

class Product(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,  # Связь с пользователем (используем настроенную модель пользователя)
        on_delete=models.CASCADE,
        related_name='products'  # Связь с продуктами пользователя
    )
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    condition = models.CharField(max_length=50)
    characteristics = models.TextField()
    photo = models.ImageField(upload_to='product_photos/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
