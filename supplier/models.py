from django.db import models
class Supplier(models.Model):
    supplier_id=models.AutoField(primary_key=True)
    supplier_name=models.CharField(max_length=255)
    supplier_status=models.CharField(max_length=255)
class Meta:
        db_table = "tbl_supplier"



 
# Create your models here.
