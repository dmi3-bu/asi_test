import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class User(AbstractUser):
    # Дефолтные поля:
    # username
    # email
    # first_name
    # last_name
    # date_joined
    # last_login
    # is_active
    # is_staff
    # is_superuser
    # groups - связь
    # user_permissions - связь
    # Кастомные поля:
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    middle_name = models.CharField(max_length=50, default='')
    date_of_birth = models.DateField(null=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True)
    phone = models.CharField(max_length=10, null=False)
