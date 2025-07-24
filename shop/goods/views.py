from django.shortcuts import render, get_list_or_404, get_object_or_404
from goods.models import Products, Categories
from django.core.paginator import Paginator
from django.http import Http404

def catalog(request, category_slug='all', page=1):

    if category_slug == 'all':
        goods = Products.objects.all()
    else:
        # Находим категорию по slug
        category = get_list_or_404(Categories, slug=category_slug)
        # Фильтруем товары по категории
        goods = Products.objects.filter(category=category)

    # Добавляю пагинацию
    paginator = Paginator(goods, 3)
    current_page = paginator.page(page)

    context = {
        'title': 'Home - Каталог',
        'goods': current_page,
        'slug_url': category_slug
    }
    return render(request, 'goods/catalog.html', context)


def product(request, product_id=None, product_slug=None):
    if product_id:
        product = get_object_or_404(Products, id=product_id)
    elif product_slug:
        product = get_object_or_404(Products, slug=product_slug)
    else:
        raise Http404("Product not found")

    context = {
        'product': product
    }
    return render(request, 'goods/product.html', context)