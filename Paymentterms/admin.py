from django.contrib import admin

from .models import Paymentterms

# Register your models here.

class PaymenttermsAdmin(admin.ModelAdmin):
    list_display = ('Paymentterms_id','Paymentterms_name','Paymentterms_slug')
admin.site.register(Paymentterms,PaymenttermsAdmin)