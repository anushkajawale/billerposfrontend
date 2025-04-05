from django.db import models
from autoslug import AutoSlugField

class Sales(models.Model):
    Sales_id = models.AutoField(primary_key=True)
    Sales_name = models.CharField(max_length=255)  # Customer Name
    Sales_invoice_no = models.CharField(max_length=100, null=True, blank=True)  # NEW: Invoice No
    Sales_addcashsale = models.BooleanField(default=False)
    Sales_add_creditsale = models.BooleanField(default=False)
    Sales_addcash = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    Sales_addcredit = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    Sales_addinvoicedate = models.DateField(null=True, blank=True)  # Invoice Date
    Sales_add_duedays = models.IntegerField(null=True, blank=True)
    Sales_add_duedate = models.DateField(null=True, blank=True)
    Sales_addproductname = models.CharField(max_length=255, null=True, blank=True)
    Sales_qty = models.IntegerField(null=True, blank=True)  # NEW: Quantity
    Sales_payment_term = models.CharField(max_length=100, null=True, blank=True)  # NEW: Payment Term
    Sales_grand_total = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)  # NEW: Grand Total
    Sales_slug = AutoSlugField(populate_from="Sales_name", unique=True)

    class Meta:
        db_table = "tbl_Sales"

    def __str__(self):
        return self.Sales_name
