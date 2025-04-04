from django.db import models
from product.models import Product
pos_id=models.AutoField(primary_key=True)
invoice_no = models.CharField(max_length=20)
customer_name = models.CharField(max_length=255)
bill_date = models.DateField()
products = models.ManyToManyField(Product)  # Link POSBill to Products
qty = models.IntegerField()
grand_total = models.DecimalField(max_digits=10, decimal_places=2)
payment_mode = models.CharField(max_length=50)

# Create your models here.
