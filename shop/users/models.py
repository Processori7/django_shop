from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    image = models.ImageField(upload_to="users_image", null=True, blank=True, verbose_name="Аватар")

    class Meta:
        db_table = 'user'
        verbose_name = 'Пользователи'
        verbose_name_plural = 'Пользователи'

    # Вывожу названия категорий
    def __str__(self):
        return self.username
