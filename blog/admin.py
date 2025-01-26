from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'author', 'publish', 'status'] # перечень отображаемых полей
    list_filter = ['status', 'created', 'publish', 'author'] # правая боковая панель для фильрации
    search_fields = ['title', 'body'] # включение строки поиска в административном интерфейсе
    prepopulated_fields = {'slug': ('title',)} # автоматическое заполнение slug при вводе значения в title
    raw_id_fields = ['author'] # реализует виджет в отдельном окне для добавления автора
    date_hierarchy = 'publish'
    ordering = ['status', 'publish'] # порядок сортировки в админке по умолчанию