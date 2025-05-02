from rest_framework import viewsets, mixins
from .models import User
from .serializers import RegisterSerializer
from drf_spectacular.utils import extend_schema


class RegisterViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

    @extend_schema(
        summary="Регистрация пользователя",
        description="Регистрирует нового пользователя на основе переданных данных: email, имя и номер телефона.",
        request=RegisterSerializer,
        responses={201: RegisterSerializer}
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
