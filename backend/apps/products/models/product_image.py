from django.db import models

from apps.common.models import BaseModel
from .product import Product


class ProductImage(BaseModel):
    """
    Stores multiple images for a product.
    """

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="images",
    )

    image = models.ImageField(
        upload_to="products/",
    )

    alt_text = models.CharField(
        max_length=255,
        blank=True,
    )

    is_primary = models.BooleanField(
        default=False,
    )

    display_order = models.PositiveIntegerField(
        default=1,
    )

    def __str__(self):
        return f"{self.product.name} ({self.display_order})"

    class Meta:
        ordering = ["display_order"]
        verbose_name = "Product Image"
        verbose_name_plural = "Product Images"