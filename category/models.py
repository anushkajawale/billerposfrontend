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
    
    def to_dict(self):
        return {
            "category_id": self.category_id,
            "category_name": self.category_name,
            "category_img": self.category_img,
            "category_bannerimg": self.category_bannerimg
        }
# Create your models here.
