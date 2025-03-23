from django.db import models
class Customergroup(models.Model):
    customergroup_id =models.AutoField(primary_key=True)
    customergroup_name= models.CharField(max_length=255) 
    
    
    class Meta:
        db_table = "tbl_customergroup"
# Create your models here.
