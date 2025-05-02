from rest_framework import serializers
from .models import Collection

class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ['id', 'author', 'title', 'description', 'photo', 'target_amount', 'collected_amount', 'status', 'completed_at', 'created_at', 'updated_at']
        
    # Если нужно преобразовать путь к изображению в URL (например, для фронтенда):
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        # Для поля photo добавляем абсолютный URL
        if instance.photo:
            representation['photo'] = instance.photo.url
        return representation

