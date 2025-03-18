from django.db import models
from autoslug import AutoSlugField

class Roles(models.Model):
    Roles_id = models.AutoField(primary_key=True)
    Roles_name = models.CharField(max_length=255)
    Roles_slug = AutoSlugField(populate_from="Roles_name",unique=True)
    class Meta:
        db_table="tbl_Roles"
        