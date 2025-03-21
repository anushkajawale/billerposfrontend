from django.contrib import admin
from .models import Supplier

class SupplierAdmin(admin.ModelAdmin):
    list_display = ('supplier_name','supplier_mobile','supplier_email','supplier_gstno','supplier_panno',' supplier_openingbal',' supplier_grouptype','supplier_BillingAddress','supplier_ShippingAddress',' supplier_City',' supplier_CreditLimit',' supplier_CreditPeriod')
admin.site.register(Supplier,SupplierAdmin)
# Register your models here.
