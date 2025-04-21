from django.db import models


class BillWiselist(models.Model):
    date = models.DateField()
    bill_no = models.CharField(max_length=100)
    customer_name = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField()
    mrp = models.DecimalField(max_digits=10, decimal_places=2)
    purchase_price = models.DecimalField(max_digits=10, decimal_places=2)
    sale_price = models.DecimalField(max_digits=10, decimal_places=2)
    profit_loss = models.DecimalField(max_digits=10, decimal_places=2)
    percentage = models.DecimalField(max_digits=5, decimal_places=2)
   

    def __str__(self):
        return f"Outstanding Report - {self.bill_no} - {self.customer_name}"
