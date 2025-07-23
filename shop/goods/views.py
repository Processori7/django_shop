from django.shortcuts import render
from goods.models import Products

def catalog(request):
    context = {
        'title':'Home - Каталог',
    }
    return render(request, 'goods/catalog.html', context)


def product(request):
    return render(request, 'goods/product.html')