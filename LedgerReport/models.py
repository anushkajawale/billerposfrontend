from django.db import models

class LedgerReport(models.Model):
    SALE_TYPE_CHOICES = (
        ('Cash', 'Cash Sale'),
        ('Credit', 'Credit Sale'),
    )

    date = models.DateField()
    sale_type = models.CharField(max_length=10, choices=SALE_TYPE_CHOICES)
    name = models.CharField(max_length=100)
    invoice_no = models.CharField(max_length=50)
    debit = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    credit = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    balance = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)


    def __str__(self):
        return f"{self.date} - {self.invoice_no} - {self.name}"
