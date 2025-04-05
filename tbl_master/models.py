from django.db import models
from customer.models import Customer
class Master(models.Model):
    master_id =models.AutoField(primary_key=True)
    customer_id= models.ForeignKey(Customer,null=True, on_delete=models.CASCADE)
    master_itemname=models.CharField(max_length=255)
    master_qty=models.CharField(max_length=255)
    master_mrp=models.CharField(max_length=255)
    master_sale_price=models.CharField(max_length=255)
    master_total =models.IntegerField()
    master_payment_mode =models.CharField(max_length=255)
    master_remaingamt =models.IntegerField()
    master_billdate =models.DateTimeField()
    master_totalAmount=models.IntegerField()

    class Meta:
        db_table = "tbl_master"


    
	# order_m_total_price
	# order_m_address
	# order_m_date
	# order_m_status ( default 1 = Pending )
	# order_m_payment_term ( default 1 = Cash On Delivery )
	# order_m_payment_status ( default 1 = Not Paid )	


# Create your models here.
