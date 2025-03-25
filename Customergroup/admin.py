from django.contrib import admin
from .models import Customergroup



class CustomergroupAdmin(admin.ModelAdmin):
    list_display =('customergroup_id','customergroup_name')
admin.site.register(Customergroup,CustomergroupAdmin) 

# Register your models here.
