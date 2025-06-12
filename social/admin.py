from django.contrib import admin
from .models import Photo  
from .models import Collection

from django.contrib import admin
from .models import Collection

@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'target_amount', 'collected_amount', 'status', 'completed_at', 'created_at')
    
    list_filter = ('status', 'created_at')
    search_fields = ('title', 'description', 'author__username')
    readonly_fields = ('collected_amount', 'created_at', 'updated_at')


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'collection', 'created_at')  # какие поля показывать в списке
    readonly_fields = ('image_preview',)  # для превью фото (ниже)
    fields = ('title', 'collection', 'image', 'image_preview')  # какие поля показывать в форме

    def image_preview(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="150" />')
        return ''
    image_preview.short_description = 'Preview'

# Если mark_safe не импортирован, импортируй
from django.utils.safestring import mark_safe
