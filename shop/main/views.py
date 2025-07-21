from django.http import HttpResponse
from django.shortcuts import render

# Получаю URL из БД и помещаю их в base.html
from goods.models import Categories


def index(request):

    # Получил категории все
    categories = Categories.objects.all()

    context = {
        "title":"Главная страница",
        "content":"Home - магазин мебели",
        "categories":categories
    }
    return render(request, "main/index.html", context)

def about(request):
    context = {
        "title": "О нас",
        "content": "О нас",
        "text_on_page":"Очень интересное описание товара"
    }
    return render(request, "main/about.html", context)

