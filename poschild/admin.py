from django.contrib import admin
from .models import Poschild
class PoschildAdmin(admin.ModelAdmin):
    list_display =('posch_id','master_id','customer_id','product_id','item_name','item_qty','item_mrp','item_saleprice','item_total')
admin.site.register(Poschild,PoschildAdmin)

# Register your models here.
