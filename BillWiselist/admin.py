from django.contrib import admin
from .models import BillWiselist

class BillWiselistAdmin(admin.ModelAdmin):
    list_display = (
        'date', 'bill_no', 'customer_name', 'quantity', 'mrp',
        'purchase_price', 'sale_price', 'profit_loss',
        'percentage'
    )

admin.site.register(BillWiselist, BillWiselistAdmin)
