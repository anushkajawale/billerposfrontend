from django.db import models
class Tax(models.Model):
    tax_id =models.AutoField(primary_key=True)
    tax_name= models.CharField(max_length=255)
    tax_percentage =models.IntegerField(null=True)
    
    
    
    class Meta:
        db_table = "tbl_tax"  

    def __str__(self):
        return self.tax_name    
# Create your models here.
