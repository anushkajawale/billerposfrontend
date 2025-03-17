from django.db import models
from autoslug import AutoSlugField

class Paymentmode(models.Model):
    Paymentmode_id = models.AutoField(primary_key=True)
    Paymentmode_name = models.CharField(max_length=255)
    Paymentmode_slug = AutoSlugField(populate_from="Paymentmode_name",unique=True)
    class Meta:
        db_table="tbl_Paymentmode"
        