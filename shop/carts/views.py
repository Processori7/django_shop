from django.shortcuts import render
from django.shortcuts import redirect
from goods.models import Products
from carts.models import Cart


def cart_detail(request):
    """Отображение страницы корзины"""
    return render(request, 'carts/cart.html')

def cart_add(request, product_slug):
    product: Products = Products.objects.get(slug=product_slug)

    if request.user.is_authenticated:
        carts = Cart.objects.filter(user=request.user, product=product)

        if carts.exists():
            cart = carts.first()
            if cart:
                cart.quantity += 1
                cart.save()
        else:
            Cart.objects.create(user=request.user, product=product, quantity=1)
            
    return redirect(request.META['HTTP_REFERER'])

def cart_change(request, product_slug):
    ...

def cart_delete(request, product_slug):
    ...
