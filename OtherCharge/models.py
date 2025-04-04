from django.db import models
from autoslug import AutoSlugField


class OtherCharge(models.Model):
    othercharge_id = models.AutoField(primary_key=True)
    othercharge_name = models.CharField(max_length=255)
    othercharge_type = models.CharField(max_length=255)
    othercharge_amount = models.CharField(max_length=255)
    othercharge_slug = AutoSlugField(populate_from="othercharge_name", unique=True)
class Meta:
     db_table = "tbl_othercharge"  