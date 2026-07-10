from django.contrib import admin

from .models import Product, ProductImage, ProductVariant


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1


class ProductVariantInline(admin.TabularInline):
    model = ProductVariant
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "vendor",
        "brand",
        "category",
        "status",
        "is_active",
    )

    list_filter = (
        "status",
        "brand",
        "category",
    )

    search_fields = ("name",)

    prepopulated_fields = {"slug": ("name",)}

    inlines = [
        ProductImageInline,
        ProductVariantInline,
    ]
