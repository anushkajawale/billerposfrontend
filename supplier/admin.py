from django.contrib import admin
from .models import Supplier

class SupplierAdmin(admin.ModelAdmin):
    list_display = ('supplier_id','supplier_name','supplier_status')
admin.site.register(Supplier,SupplierAdmin)
# Register your models here.
