from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # первый аргумент - путь, namespace позволяет организовать уникальную ссылку на тот или иной url
    path('', include('main.urls', namespace='main'))
]
