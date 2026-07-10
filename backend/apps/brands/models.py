from django.db import models

from apps.categories.models import Category
from apps.common.models import BaseModel


class Brand(BaseModel):
    """
    Brand master data.
    """

    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        related_name="brands",
    )

    name = models.CharField(
        max_length=100,
        unique=True,
    )

    slug = models.SlugField(
        unique=True,
    )

    logo = models.ImageField(
        upload_to="brands/",
        blank=True,
        null=True,
    )

    description = models.TextField(
        blank=True,
    )

    website = models.URLField(
        blank=True,
    )

    is_active = models.BooleanField(
        default=True,
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]
        verbose_name = "Brand"
        verbose_name_plural = "Brands"