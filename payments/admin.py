from django.contrib import admin
from .models import Collection

class CollectionAdmin(admin.ModelAdmin):

    list_display = ('id', 'title', 'author', 'status', 'target_amount', 'collected_amount', 'created_at', 'updated_at', 'photo_preview')
    

    list_filter = ('status', 'author')
    
    # Функция для отображения превью изображения
    def photo_preview(self, obj):
        if obj.photo:
            return f'<img src="{obj.photo.url}" width="100" height="100" />'  # Превью изображения
        return 'Нет изображения'
    
    # Разрешаем использовать html в админке для превью
    photo_preview.allow_tags = True
    photo_preview.short_description = 'Фото'

    # Выбираем поля, которые будут доступны для редактирования
    fields = ['author', 'title', 'description', 'photo', 'target_amount', 'collected_amount', 'status', 'completed_at']
    
    # Выбираем поля для отображения в редактировании
    search_fields = ('title', 'author__email')

# Регистрируем модель в админке
admin.site.register(Collection, CollectionAdmin)
