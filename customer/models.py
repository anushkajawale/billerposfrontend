from django.db import models
class Customer(models.Model):
    customer_id=models.AutoField(primary_key=True)
    customer_name=models.CharField(max_length=255)
    customer_status=models.CharField(max_length=255)
class Meta:
        db_table = "tbl_customer"



 
# Create your models here.
