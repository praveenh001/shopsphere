from django.contrib.auth.models import AbstractUser
from django.db import models

from .managers import UserManager


class Role(models.TextChoices):
    ADMIN = "ADMIN", "Admin"
    VENDOR = "VENDOR", "Vendor"
    CUSTOMER = "CUSTOMER", "Customer"


class User(AbstractUser):
    username = models.CharField(
        max_length=150,
        blank=True,
        null=True,
    )

    email = models.EmailField(
        unique=True,
    )

    phone_number = models.CharField(
        max_length=15,
        blank=True,
    )

    profile_image = models.ImageField(
        upload_to="profiles/",
        blank=True,
        null=True,
    )

    role = models.CharField(
        max_length=20,
        choices=Role.choices,
        default=Role.CUSTOMER,
    )

    is_verified = models.BooleanField(
        default=False,
    )

    objects = UserManager()

    USERNAME_FIELD = "email"

    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return self.email
    
    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"