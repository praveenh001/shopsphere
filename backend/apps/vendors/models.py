from django.conf import settings
from django.db import models
from apps.common.models import BaseModel


class Vendor(BaseModel):
    """
    Vendor profile linked to a user.
    """

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="vendor_profile",
    )

    store_name = models.CharField(
        max_length=255,
        unique=True,
    )

    business_name = models.CharField(
        max_length=255,
    )

    gst_number = models.CharField(
        max_length=50,
        unique=True,
    )

    pan_number = models.CharField(
        max_length=20,
        unique=True,
    )

    phone_number = models.CharField(
        max_length=15,
    )

    business_email = models.EmailField(
        unique=True,
    )

    description = models.TextField(
        blank=True,
    )

    logo = models.ImageField(
        upload_to="vendors/logos/",
        blank=True,
        null=True,
    )

    banner = models.ImageField(
        upload_to="vendors/banners/",
        blank=True,
        null=True,
    )

    address = models.TextField()

    city = models.CharField(
        max_length=100,
    )

    state = models.CharField(
        max_length=100,
    )

    country = models.CharField(
        max_length=100,
        default="India",
    )

    postal_code = models.CharField(
        max_length=10,
    )

    is_approved = models.BooleanField(
        default=False,
    )

    approved_at = models.DateTimeField(
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.store_name

    class Meta:
        ordering = ["store_name"]
        verbose_name = "Vendor"
        verbose_name_plural = "Vendors"
