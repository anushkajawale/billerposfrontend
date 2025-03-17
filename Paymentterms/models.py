from django.db import models
from autoslug import AutoSlugField

class Paymentterms(models.Model):
    Paymentterms_id = models.AutoField(primary_key=True)
    Paymentterms_name = models.CharField(max_length=255)
    Paymentterms_slug = AutoSlugField(populate_from="Paymentterms_name",unique=True)
    class Meta:
        db_table="tbl_Paymentterms"