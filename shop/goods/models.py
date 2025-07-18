from django.db import models

class Categories(models.Model):
    # Поле ID создаётся автоматически
    name = models.CharField(max_length=150, unique=True, verbose_name="Название")
    slug = models.SlugField(max_length=300, unique=True, blank=True, null=True, verbose_name="URL")  # blank=True - поле может быть пустым, null=True - связано с blank
    
    class Meta:
        db_table = 'category'
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
