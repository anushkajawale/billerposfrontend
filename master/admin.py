from django.contrib import admin
from .models import Master

class MasterAdmin(admin.ModelAdmin):
    list_display =('master_id','customer_id','master_payment_mode','master_billdate','master_totalAmount')
admin.site.register(Master,MasterAdmin) 
# Register your models here.

# Register your models here.
