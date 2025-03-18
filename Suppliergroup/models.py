from django.db import models
class Suppliergroup(models.Model):
    suppliergroup_id =models.AutoField(primary_key=True)
    suppliergroup_name= models.CharField(max_length=255) 
    
    
    class Meta:
        db_table = "tbl_suppliergroup"
# Create your models here.
