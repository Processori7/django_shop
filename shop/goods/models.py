from django.db import models

class Categories(models.Model):
    # Поле ID создаётся автоматически
    name = models.CharField(max_length=150, unique=True, verbose_name="Название")
    slug = models.SlugField(max_length=300, unique=True, blank=True, null=True, verbose_name="URL")  # blank=True - поле может быть пустым, null=True - связано с blank
    
    class Meta:
        db_table = 'category'
        verbose_name = 'Категорию'
        verbose_name_plural = 'Категории'

# Вывожу названия категорий
    def __str__(self):
        return self.name
    
class Products(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name="Название")
    slug = models.SlugField(max_length=300, unique=True, blank=True, null=True, verbose_name="URL")  # blank=True - поле может быть пустым, null=True - связано с blank
    description = models.TextField( blank=True, null=True, verbose_name="Описание")
    image = models.ImageField(upload_to="goods_images", blank=True, null=True)
    price = models.DecimalField(default=0.00, max_digits=7, decimal_places=2, verbose_name="Цена")
    discount = models.DecimalField(default=0.00, max_digits=7, decimal_places=2, verbose_name="Скидка")
    quantity = models.PositiveIntegerField(default=0, verbose_name="Колличество")
    category = models.ForeignKey(to=Categories, on_delete=models.PROTECT)

    class Meta:
        db_table = 'product'
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    # Вывожу названия продуктов и их кол-во
    def __str__(self):
         return f"{self.name}. В наличии: ({self.quantity} шт.)"