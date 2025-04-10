from django.db import models
from customer.models import Customer
class Master(models.Model):
    master_id =models.AutoField(primary_key=True)
    customer_id= models.ForeignKey(Customer,null=True, on_delete=models.CASCADE)
    master_payment_mode =models.CharField(max_length=255)    
    master_billdate =models.DateTimeField()
    master_totalAmount=models.IntegerField()

    class Meta:
        db_table = "tbl_master"

# Create your models here.
