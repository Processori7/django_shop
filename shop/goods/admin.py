from django.contrib import admin

# Register your models here.
from goods.models import Categories, Products

# admin.site.register(Categories)
# admin.site.register(Products)

# Добавляю URL 
@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    # Переменная для указания полей, которые будут заполняться автоматически
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    # Переменная для указания полей, которые будут заполняться автоматически
    prepopulated_fields = {'slug': ('name',)}