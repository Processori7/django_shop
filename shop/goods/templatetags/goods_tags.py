# goods/templatetags/custom_tags.py
from goods.models import Products, Categories
from django import template

from django.utils.http import urlencode

register = template.Library()  # должно быть template.Library()

# Простой тег для получения всех категорий
@register.simple_tag()
def tag_categories():
    return Categories.objects.all()

# Простой тег для получения всех продуктов
# @register.simple_tag()
# def tag_products():
#     return Products.objects.all()

@register.simple_tag(takes_context=True)
def change_params(context, **kwargs):
   query = context['request'].GET.dict()
   query.update(kwargs)
   return urlencode(query)