from django.db import models

from apps.common.models import BaseModel
from .product import Product


class ProductVariant(BaseModel):
    """
    Represents a purchasable variant of a product.
    """

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="variants",
    )

    sku = models.CharField(
        max_length=100,
        unique=True,
    )

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
    )

    discount_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True,
    )

    color = models.CharField(
        max_length=100,
        blank=True,
    )

    size = models.CharField(
        max_length=50,
        blank=True,
    )

    storage = models.CharField(
        max_length=50,
        blank=True,
    )

    weight = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        null=True,
        blank=True,
    )

    barcode = models.CharField(
        max_length=100,
        blank=True,
    )

    is_active = models.BooleanField(
        default=True,
    )

    def __str__(self):
        return f"{self.product.name} - {self.sku}"

    class Meta:
        ordering = ["sku"]
        verbose_name = "Product Variant"
        verbose_name_plural = "Product Variants"