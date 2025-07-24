# goods/templatetags/custom_tags.py
from goods.models import Products, Categories
from django import template

register = template.Library()  # должно быть template.Library()

# Простой тег для получения всех категорий
@register.simple_tag()
def tag_categories():
    return Categories.objects.all()

# Простой тег для получения всех продуктов
# @register.simple_tag()
# def tag_products():
#     return Products.objects.all()
