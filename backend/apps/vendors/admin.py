from django.contrib import admin

from .models import Vendor


@admin.register(Vendor)
class VendorAdmin(admin.ModelAdmin):
    list_display = (
        "store_name",
        "business_name",
        "business_email",
        "is_approved",
    )

    list_filter = (
        "is_approved",
        "state",
    )

    search_fields = (
        "store_name",
        "business_name",
        "gst_number",
    )