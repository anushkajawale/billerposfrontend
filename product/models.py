from django.db import models
from category.models import Category
from brand.models import Brand
from Unit.models import Unit
from tax.models import Tax
class Product(models.Model):
    product_id =models.AutoField(primary_key=True)
    product_name= models.CharField(max_length=255)
    product_MarathiName=models.CharField(max_length=255)
    product_HSNCode =models.IntegerField()
    category=models.ForeignKey(Category,null=True)  
    brand=models.ForeignKey(Brand,null=True)  
    tax=models.ForeignKey(Tax,null=True)
    taxpercent=models.ForeignKey(Tax,null=True)
    taxtype=models.ForeignKey(Tax,null=True)
    unit=models.ForeignKey(Unit,null=True)
    alternateunit=models.IntegerField()
    conversionfact=models.IntegerField()
    




    
    
    class Meta:
        db_table = "tbl_category"


# Create your models here.
