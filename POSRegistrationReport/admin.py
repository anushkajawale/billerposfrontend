from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import POSRegistrationReport

class POSRegistrationReportAdmin(admin.ModelAdmin):
    list_display = ('id', 'date', 'sale_type', 'name', 'invoice_no', 'debit', 'credit', 'balance')
    list_filter = ('sale_type', 'date')
    search_fields = ('name', 'invoice_no')

admin.site.register(POSRegistrationReport, POSRegistrationReportAdmin)
