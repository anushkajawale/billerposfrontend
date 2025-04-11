from django.contrib import admin

from .models import Sales



class SalesAdmin(admin.ModelAdmin):
    list_display = (
        'Sales_id', 'Sales_addinvoicedate', 'Sales_invoice_no', 'Sales_name', 'Sales_qty', 'Sales_payment_term', 'Sales_mrp',
        'Sales_discount_percent','Sales_discount_value','Sales_basic_total','Sales_gst_percent','Sales_gst_value','Sales_grand_total','Sales_price'
    )

admin.site.register(Sales, SalesAdmin)
