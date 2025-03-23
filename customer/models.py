from django.db import models
class Customer(models.Model):
    customer_id=models.AutoField(primary_key=True)
    customer_name=models.CharField(max_length=255,null=True)
    customer_mobile=models.IntegerField(null=True)
    customer_email=models.CharField(max_length=255,null=True)
    customer_gstno=models.IntegerField(null=True)
    
    customer_panno=models.IntegerField(null=True)
    customer_openingbal=models.IntegerField(null=True)
    customer_grouptype=models.CharField(max_length=255,null=True)
    customer_BillingAddress=models.CharField(max_length=255,null=True)
    customer_ShippingAddress=models.CharField(max_length=255,null=True)
    customer_City=models.CharField(max_length=255,null=True)
    customer_CreditLimit=models.IntegerField(null=True)
    customer_CreditPeriod=models.IntegerField(null=True) 
    class Meta:
        db_table = "tbl_customer"



 
# Create your models here.
