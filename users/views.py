from rest_framework import viewsets, mixins
from .models import User
from .serializers import RegisterSerializer
from drf_spectacular.utils import extend_schema
# from utils.exception_handler import success_registration_response

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
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        # return success_registration_response()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
