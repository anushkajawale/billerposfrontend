from django.contrib import admin
from .models import Master

class MasterAdmin(admin.ModelAdmin):
    list_display =('customer_id','master_itemname','master_qty','master_mrp','master_sale_price','master_total','master_payment_mode','master_billdate','master_totalAmount')
admin.site.register(Master,MasterAdmin) 
# Register your models here.
