from django.contrib import admin
from .models import Customer

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('customer_id','customer_name','customer_status')
admin.site.register(Customer,CustomerAdmin)
# Register your models here.
    