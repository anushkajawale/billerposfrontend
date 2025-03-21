from django.contrib import admin
from .models import Tax



class TaxAdmin(admin.ModelAdmin):
    list_display =('tax_name','tax_percentage')
admin.site.register(Tax,TaxAdmin) 

# Register your models here.
