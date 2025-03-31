from django.db import models

# Create your models here.

class RewardPoints(models.Model):
    RewardPoints_id=models.AutoField(primary_key=True)
    
    RewardPoints_Maxrange=models.IntegerField(null=True)          
    
    RewardPoints_Minrange=models.IntegerField(null=True)

    RewardPoints_Points=models.IntegerField(null=True)


    
    

    class Meta:
        db_table = "tbl_RewardPoints"



 
# Create your models here.