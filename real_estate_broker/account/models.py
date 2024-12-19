from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models

from real_estate_broker.account.managers import CustomerManager


# Create your models here.

class CustomerModel(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(
        max_length=150,
        unique=True
    )
    email = models.EmailField(
        unique=True,
        blank=False,
        null=False
    )
    first_name = models.CharField(
        max_length=50,
        blank=True,
        null=True
    )
    last_name = models.CharField(
        max_length=50,
        blank=True,
        null=True
    )
    youtube_video_url = models.URLField(
    )

    is_active = models.BooleanField(
        default=True,
    )

    is_staff = models.BooleanField(
        default=False,
    )

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]

    objects = CustomerManager()

    def __str__(self):
        return self.username