from django.contrib import admin

from .models import Reward


@admin.register(Reward)
class RewardAdmin(admin.ModelAdmin):
    list_display = ("customer", "reward_type", "claimed", "created_at", "claimed_at")
    search_fields = ("customer__name", "customer__email", "customer__phone", "reward_type")
    list_filter = ("claimed", "created_at", "claimed_at")