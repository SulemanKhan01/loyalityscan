from django.db import models
from django.utils import timezone

from customers.models import Customer


class Reward(models.Model):
    customer = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE,
        related_name="rewards",
    )
    reward_type = models.CharField(max_length=100, default="Free Coffee")
    created_at = models.DateTimeField(auto_now_add=True)
    claimed = models.BooleanField(default=False)
    claimed_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        status = "claimed" if self.claimed else "available"
        return f"{self.reward_type} for {self.customer.name} ({status})"

    def mark_claimed(self):
        self.claimed = True
        self.claimed_at = timezone.now()
        self.save(update_fields=["claimed", "claimed_at"])