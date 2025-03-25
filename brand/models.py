from django.db import models
class Brand(models.Model):
    brand_id =models.AutoField(primary_key=True)
    brand_name= models.CharField(max_length=255)
    brand_img =models.ImageField(upload_to='brand/')
    
    
    
    class Meta:
        db_table = "tbl_brand"  

# Create your models here.
