from django.contrib import admin
from .models import RewardPoints

class RewardPointsAdmin(admin.ModelAdmin):
    list_display = ['RewardPoints_id','RewardPoints_Maxrange','RewardPoints_Minrange','RewardPoints_Points']
admin.site.register(RewardPoints,RewardPointsAdmin)
# Register your models here.
