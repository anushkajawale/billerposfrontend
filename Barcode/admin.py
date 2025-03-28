from django.contrib import admin
from .models import Barcode

class BarcodeAdmin(admin.ModelAdmin):
    list_display =('barcode_number','barcode_img')
admin.site.register(Barcode,BarcodeAdmin) 

# Register your models here.
