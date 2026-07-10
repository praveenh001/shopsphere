from django.db import models

from apps.common.models import BaseModel
from .product_variant import ProductVariant


class Inventory(BaseModel):
    """
    Inventory for a product variant.
    """

    variant = models.OneToOneField(
        ProductVariant,
        on_delete=models.CASCADE,
        related_name="inventory",
    )

    quantity = models.PositiveIntegerField(
        default=0,
    )

    reserved_quantity = models.PositiveIntegerField(
        default=0,
    )

    low_stock_threshold = models.PositiveIntegerField(
        default=5,
    )

    @property
    def available_quantity(self):
        return self.quantity - self.reserved_quantity

    def __str__(self):
        return f"{self.variant.sku} Inventory"

    class Meta:
        verbose_name = "Inventory"
        verbose_name_plural = "Inventory"