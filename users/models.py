from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

class User(AbstractUser):
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, unique=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'phone_number']

    groups = models.ManyToManyField(
        Group,
        related_name="costumuser_groups",
        blank=True,
    )

    user_permissions = models.ManyToManyField(
        Permission,
        related_name="costumuser_permission",
        blank=True,
    )

    def __str__(self):
        return self.email