from django.contrib import admin

from .models import Scan


@admin.register(Scan)
class ScanAdmin(admin.ModelAdmin):
    list_display = ("customer", "scanned_at")
    search_fields = ("customer__name", "customer__email", "customer__phone")
    list_filter = ("scanned_at",)