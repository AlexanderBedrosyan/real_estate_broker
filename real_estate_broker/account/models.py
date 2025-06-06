from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from real_estate_broker.main_app.validators import IsItAPhoneNumber
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
        blank=False,
        null=False
    )
    last_name = models.CharField(
        max_length=50,
        blank=False,
        null=False
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


class Contact(models.Model):

    account = models.OneToOneField(
        to=CustomerModel,
        on_delete=models.CASCADE,
        related_name='contacts'
    )
    phone_number = models.CharField(
        max_length=100,
        blank=False,
        null=False,
        validators=[IsItAPhoneNumber()]
    )
    facebook_page = models.URLField(
        blank=False,
        null=False
    )
    email = models.EmailField(
        blank=False,
        null=False
    )

    def __str__(self):
        return self.account.first_name + ' ' + self.account.last_name
