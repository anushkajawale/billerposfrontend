from django.db import models

class ReportOutstanding(models.Model):
    customer_name = models.CharField(max_length=255)
    city = models.CharField(max_length=100, blank=True, null=True)
    mobile = models.CharField(max_length=15, blank=True, null=True)
    balance = models.FloatField(default=0)

    def __str__(self):
        return f"{self.customer_name} ({self.city})"
