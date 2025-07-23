from django.shortcuts import render
from goods.models import Products

def catalog(request):
    context = {
        'title':'Home - Каталог',
    }
    return render(request, 'goods/catalog.html', context)


def product(request, product_id=False, product_slug=False):

    if product_id:
        product = Products.objects.get(id=product_id)
    else:
        product = Products.objects.get(slug=product_slug)
        
    context = {
        'product': product
    }
    return render(request, 'goods/product.html', context)