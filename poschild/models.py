from django.db import models
from master.models import Master
from customer.models import Customer
from product.models import Product
class Poschild(models.Model):

    posch_id =models.AutoField(primary_key=True)
    master_id =models.ForeignKey(Master,on_delete=models.CASCADE)
    customer_id= models.ForeignKey(Customer, on_delete=models.CASCADE)
    product_id= models.ForeignKey(Product, on_delete=models.CASCADE) 
    item_name=models.CharField(max_length=255)
    item_qty=models.IntegerField()
    item_mrp=models.FloatField(default=0.0)
    item_saleprice=models.FloatField(default=0.0)
    item_total=models.FloatField(default=0.0)


   
    

    class Meta:
        db_table = "tbl_poschild"

# Create your models here.
