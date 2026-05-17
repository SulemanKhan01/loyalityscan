from django.contrib import admin
from django.db.models import Count

from .models import Customer


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "phone", "scan_count", "created_at")
    search_fields = ("name", "email", "phone")
    list_filter = ("created_at",)

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset.annotate(total_scans=Count("scans"))

    def scan_count(self, obj):
        return obj.total_scans

    scan_count.admin_order_field = "total_scans"