from django.db import models
from category.models import Category
from brand.models import Brand
from Unit.models import Unit
from tax.models import Tax
from Barcode.models import Barcode
class Product(models.Model):    
    product_id =models.AutoField(primary_key=True)
    product_name= models.CharField(max_length=255)
    product_marathi_name=models.CharField(max_length=255)
    product_HSNCode =models.CharField(max_length=255)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)  
    brand=models.ForeignKey(Brand,null=True,on_delete=models.CASCADE)  
    tax=models.ForeignKey(Tax,null=True,on_delete=models.CASCADE)
    taxpercent=models.CharField(max_length=255)
    taxtype=models.CharField(max_length=255)
    unit=models.ForeignKey(Unit,null=True,on_delete=models.CASCADE)  
    alternateunit=models.IntegerField()
    conversionfact=models.FloatField()
    nos=models.IntegerField()
    barcode=models.ForeignKey(Barcode,null=True,on_delete=models.CASCADE)
    qrcode=models.IntegerField()
    mrp=models.DecimalField(max_digits=10, decimal_places=2)   
    sale=models.DecimalField(max_digits=10, decimal_places=2)   
    credit=models.DecimalField(max_digits=10, decimal_places=2)
    purchase=models.IntegerField()    
    wholesaler=models.IntegerField()    
    distributor=models.IntegerField()    
    op_Qty=models.IntegerField()    
    op_Value=models.IntegerField()    
    mfg_Date=models.DateField()    
    exp_Date=models.DateField()     
    class Meta:
        db_table = "tbl_product"

    def __str__(self):
        return self.product_name    


# Create your models here.
