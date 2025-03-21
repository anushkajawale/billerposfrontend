from django.contrib import admin
from .models import Customer

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('customer_id','customer_name','customer_mobile','customer_email','customer_gstno','customer_panno','customer_openingbal','customer_grouptype','customer_BillingAddress','customer_ShippingAddress','customer_City','customer_CreditLimit','customer_CreditPeriod')
admin.site.register(Customer,CustomerAdmin)
# Register your models here.
    