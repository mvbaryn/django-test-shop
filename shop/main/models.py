from django.db import models
from django.urls import reverse


class Category(models.Model):
    # db_index нужен для того, чтобы ускорить поиск (работает как номер страниц в книге)
    name = models.CharField(max_length=100, db_index=True)
    # slug нужен для того, чтобы сгенерировать понятное название в адресной строке
    slug = models.SlugField(max_length=100, unique=True)

    # метаданные, то есть данные о данных
    class Meta:
        # в админке все записи из этой таблицы будут отсортированы по названию
        ordering = ('name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    # функция, которая указывает на то, как следует отображать модель в админке
    def __str__(self):
        return self.name
    
    #
    def get_absolute_url(self):
        return reverse("main:product_detail", args=[self.slug])
    


class Product(models.Model):
    # наследуем поле category, то есть оно будет иметь все, что было описано в классу Category
    # releated_name - отображение в админке
    # второй параметр - что делать при удалении
    # CASCADE - позволяет удалить,PROTECT - не дает
    category = models.ForeignKey(Category, related_name='products',
                                 on_delete=models.CASCADE)
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, unique=True)
    # куда будем фотки загружать
    # blank=True - можем не добавлять фотографию, поле может быть пустое
    image = models.ImageField(upload_to='product/%Y/%m/%d', blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    # auto_now_add - дата создания, auto_now - дата обновления
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("main:product_detail",  args=[self.id, self.slug])
    