from django.db import models
class Category(models.Model):
    category_id =models.AutoField(primary_key=True)
    category_name= models.CharField(max_length=255)
    category_img =models.ImageField(upload_to='category/')
    category_bannerimg =models.ImageField(upload_to='category/')  
    
    
    class Meta:
        db_table = "tbl_category"
    
    def __str__(self):
        return self.category_name

# Create your models here.
