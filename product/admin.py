from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display =('product_name',
'product_marathi_name',
'product_HSNCode',
'category',
'brand',
'tax',
'taxpercent',
'taxtype',
'unit',
'alternateunit',
'conversionfact',
'nos',
'qrcode',
'mrp',
'sale',
'credit',
'purchase',
'wholesaler',
'distributor',
'op_Qty',
'op_Value',
'mfg_Date',
'exp_Date'
)


admin.site.register(Product,ProductAdmin) 

# Register your models here.
