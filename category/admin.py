from django.contrib import admin
from .models import Category



class CategoryAdmin(admin.ModelAdmin):
    list_display =('category_name','category_img','category_bannerimg')
admin.site.register(Category,CategoryAdmin) 

# Register your models here.
