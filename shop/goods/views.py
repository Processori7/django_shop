from django.shortcuts import render, get_object_or_404
from goods.models import Products, Categories
from django.core.paginator import Paginator
from django.http import Http404
from goods.utils import q_search


def catalog(request, category_slug=None):

    page = request.GET.get('page',1)
    on_sale = request.GET.get('on_sale', None)
    order_by = request.GET.get('order_by', None)
    query = request.GET.get('q', None)

    if category_slug == 'all':
        goods = Products.objects.all()
    elif query:
        goods = q_search(query)
    else:
        # Находим категорию по slug
        category = get_object_or_404(Categories, slug=category_slug)
        # Фильтруем товары по категории
        goods = Products.objects.filter(category=category)

    if on_sale:
        # __gt - означает >
        goods = goods.filter(discount__gt=0) 

    if order_by and order_by != 'default':
        goods = goods.order_by(order_by)

    # Добавляю пагинацию
    paginator = Paginator(goods, 3)
    current_page = paginator.page(int(page))

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