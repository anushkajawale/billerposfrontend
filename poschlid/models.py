from django.db import models
from tbl_master.models import Master
from customer.models import Customer
from product.models import Product
class Poschild(models.Model):

    posch_id =models.AutoField(primary_key=True)
    master_id =models.ForeignKey(Master,on_delete=models.CASCADE)
    customer_id= models.ForeignKey(Customer, on_delete=models.CASCADE)
    product_id= models.ForeignKey(Product, on_delete=models.CASCADE)        

   
    

    class Meta:
        db_table = "tbl_poschild"

# Create your models here.  
