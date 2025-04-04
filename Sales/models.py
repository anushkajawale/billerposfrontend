#from django.db import models
#from autoslug import AutoSlugField

"""class Paymentmode(models.Model):
    Sales_id = models.AutoField(primary_key=True)
    Sales_name = models.CharField(max_length=255)
    Sales_addcashsale =models.BooleanField(default=False)
    Sales_add_creditsale =models.BooleanField(default=False)
    Sales_addcash = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    Sales_addcredit = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    Sales_addinvoicedate = models.DateField(null=True, blank=True)
    Sales_add_duedays = models.IntegerField(null=True, blank=True)
    Sales_add_duedate = models.DateField(null=True, blank=True)
    Sales_addproductname = models.CharField(max_length=255, null=True, blank=True)
    Sales_slug = AutoSlugField(populate_from="Sales_name",unique=True)
    class Meta:
        db_table="tbl_Sales"

    def __str__(self):
        return self.""sales_name"""
    

