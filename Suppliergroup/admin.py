from django.contrib import admin
from .models import Suppliergroup



class SuppliergroupAdmin(admin.ModelAdmin):
    list_display =('suppliergroup_id','suppliergroup_name')
admin.site.register(Suppliergroup,SuppliergroupAdmin) 

# Register your models here.
