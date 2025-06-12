from rest_framework import serializers
from .models import User
from django.contrib.auth.hashers import make_password
import re

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'username', 'phone_number', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])  # Хешируем пароль
        return super().create(validated_data)


    def validate_phone_number(self, value):
       
        if not re.match(r'^\+\d{10,15}$', value):
            raise serializers.ValidationError("Введите корректный номер телефона.")
        return value