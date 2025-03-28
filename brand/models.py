from django.db import models
class Brand(models.Model):
    brand_id =models.AutoField(primary_key=True)
    brand_name= models.CharField(max_length=255)
    brand_img =models.ImageField(upload_to='brand/')
    
    
    
    class Meta:
        db_table = "tbl_brand"  
    def __str__(self):
        return self.brand_name    

# Create your models here.
