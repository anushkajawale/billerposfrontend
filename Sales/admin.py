from django.contrib import admin

from .models import Sales



class SalesAdmin(admin.ModelAdmin):
    list_display = (
        'Sales_id', 'Sales_addinvoicedate', 'Sales_invoice_no', 'Sales_name', 
        'Sales_qty', 'Sales_payment_term', 'Sales_grand_total'
    )

admin.site.register(Sales, SalesAdmin)
