from django.shortcuts import render

def cart_detail(request):
    """Отображение страницы корзины"""
    return render(request, 'carts/cart.html')

def cart_add(request, product_id):
    ...

def cart_change(request, product_id):
    ...

def cart_delete(request, product_id):
    ...
