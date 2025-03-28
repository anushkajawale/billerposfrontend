from django.db import models
from autoslug import AutoSlugField

class Roles(models.Model):
    Roles_id=models.AutoField(primary_key=True)
    Roles_name = models.CharField(max_length=255)
    Roles_Dashboard = models.BooleanField(default=False)
    Roles_UserProfile = models.BooleanField(default=False)
    Roles_BusinessProfile = models.BooleanField(default=False)  # Fix spelling (not "Bussiness")
    Roles_BarcodePrint = models.BooleanField(default=False)
    Roles_Stock = models.BooleanField(default=False)
    Roles_HRDepartment = models.BooleanField(default=False)
    Roles_RewardPoint = models.BooleanField(default=False)  # No hyphen
    Roles_POS = models.BooleanField(default=False)
    Roles_Sale = models.BooleanField(default=False)
    Roles_Purchase = models.BooleanField(default=False)
    Roles_Supplier = models.BooleanField(default=False)
    Roles_Settings = models.BooleanField(default=False)
    Roles_slug=AutoSlugField(populate_from="Roles_name",unique=True)

    class Meta:
         db_table="tbl_Roles"