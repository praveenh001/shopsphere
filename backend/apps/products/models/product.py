from django.db import models

from apps.brands.models import Brand
from apps.categories.models import Category
from apps.common.models import BaseModel
from apps.vendors.models import Vendor


class ProductStatus(models.TextChoices):
    DRAFT = "DRAFT", "Draft"
    PUBLISHED = "PUBLISHED", "Published"
    ARCHIVED = "ARCHIVED", "Archived"


class Product(BaseModel):
    """
    Master product information.
    """

    vendor = models.ForeignKey(
        Vendor,
        on_delete=models.CASCADE,
        related_name="products",
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        related_name="products",
    )

    brand = models.ForeignKey(
        Brand,
        on_delete=models.PROTECT,
        related_name="products",
    )

    name = models.CharField(
        max_length=255,
    )

    slug = models.SlugField(
        unique=True,
    )

    short_description = models.CharField(
        max_length=300,
    )

    description = models.TextField()

    status = models.CharField(
        max_length=20,
        choices=ProductStatus.choices,
        default=ProductStatus.DRAFT,
    )

    is_active = models.BooleanField(
        default=True,
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]
        verbose_name = "Product"
        verbose_name_plural = "Products"


        