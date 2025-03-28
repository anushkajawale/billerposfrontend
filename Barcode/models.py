from django.db import models

class Barcode(models.Model):
    barcode_id =models.AutoField(primary_key=True)
    barcode_number= models.IntegerField()
    barcode_img =models.ImageField(upload_to='barcode/')

    class Meta:
        db_table = "tbl_barcode"  
    def __str__(self):
        return self.barcode_number 

# Create your models here.
