from django.contrib import admin
from .models import Category, Product


# регистрируем моделт в админке
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    # параметры, которые будут отображаться в админке
    list_display = ['name', 'slug']
    # поля, которые будут заполнены автоматически
    # slug автоматически заполнится в соответствии с name
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price', 'available', 'created', 'updated']
    # параметры по которым будем фильтровать
    list_filter = ['available', 'created', 'updated', 'category']
    # параметры, которые можно изменять
    list_editable = ['price', 'available']
    prepopulated_fields = {'slug': ('name',)}