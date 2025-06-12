from rest_framework import serializers
from .models import Collection, Photo

class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ['image']


class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = '__all__'
        read_only_fields = ['author', 'collected_amount', 'created_at', 'updated_at']

    def create(self, validated_data):
        photos_data = self.context['request'].FILES.getlist('listPhoto')
        collection = Collection.objects.create(**validated_data)
        for image in photos_data:
            Photo.objects.create(collection=collection, image=image)
        return collection
