from django.db import models
class Supplier(models.Model):
    supplier_id=models.AutoField(primary_key=True)
    supplier_name=models.CharField(max_length=255,null=True)
    supplier_mobile=models.IntegerField(null=True)
    supplier_email=models.CharField(max_length=255,null=True)
    supplier_gstno=models.IntegerField(null=True)
    
    supplier_panno=models.IntegerField()
    supplier_openingbal=models.IntegerField()
    supplier_grouptype=models.CharField(max_length=255)
    supplier_BillingAddress=models.CharField(max_length=255,null=True)
    supplier_ShippingAddress=models.CharField(max_length=255,null=True)
    supplier_City=models.CharField(max_length=255,null=True)
    supplier_CreditLimit=models.IntegerField()
    supplier_CreditPeriod=models.IntegerField() 
    class Meta:
        db_table = "tbl_supplier"



 
# Create your models here.