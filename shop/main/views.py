from django.shortcuts import render, get_object_or_404
from .models import Category, Product


# categiry_slug - параметры запроса для фильтрации
def product_list(request, category_slug=None):
    # выводим все категории и продукты
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)

    category = None
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    # templates не нужно писать в пути к шаблону для рэндэра страницы
    return render(request, 'main/product/list.html',
                  {'category': category,
                   'categories': categories,
                   'products': products})


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    # похожие продукты (из той же категории), сначала фильтруем по категории, потом по доступности, потом убираем текущий товар, чтобы два раза его не выводить
    related_products = Product.objects.filter(Category=product.category,
                                              available=True).exclude(id=product.id)[:4]
    
    return render(request, 'main/product/detail.html', {'product' : product,
                                                        'related_products' : related_products})