from django.db import models
from autoslug import AutoSlugField


class Expenses(models.Model):
    expenses_id = models.AutoField(primary_key=True)
    expenses_name = models.CharField(max_length=255)
    

    expenses_slug = AutoSlugField(populate_from="expenses_name", unique=True)
class Meta:
     db_table = "tbl_expenses"  