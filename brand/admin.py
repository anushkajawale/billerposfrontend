from django.contrib import admin
from .models import Brand



class BrandAdmin(admin.ModelAdmin):
    list_display =('brand_name','brand_img')
admin.site.register(Brand,BrandAdmin) 

# Register your models here.
