from django.contrib import admin

from .models import Paymentmode

# Register your models here.

class PaymentmodeAdmin(admin.ModelAdmin):
    list_display = ('Paymentmode_id','Paymentmode_name','Paymentmode_slug')
admin.site.register(Paymentmode,PaymentmodeAdmin)