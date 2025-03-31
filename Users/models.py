from django.db import models
from autoslug import AutoSlugField

class Users(models.Model):
    users_id = models.AutoField(primary_key=True)
    users_name = models.CharField(max_length=255, default="Cash")
    users_email = models.CharField(max_length=255, null=True, blank=True)

    
    users_mobile = models.CharField(max_length=10, null=True, blank=True) 
    users_role = models.CharField(max_length=50, null=True, blank=True)
    users_pass = models.CharField(max_length=50, null=True, blank=True)
    users_slug = AutoSlugField(populate_from="users_email", unique=True)
    class Meta:
        db_table = "tbl_Users"  

