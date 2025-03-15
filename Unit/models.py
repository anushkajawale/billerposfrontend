from django.db import models
from autoslug import AutoSlugField


class Unit(models.Model):
    unit_id = models.AutoField(primary_key=True)
    unit_name = models.CharField(max_length=255)
    

    unit_slug = AutoSlugField(populate_from="unit_name", unique=True)
class Meta:
     db_table = "tbl_unit"  

