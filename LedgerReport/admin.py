from django.contrib import admin

from .models import LedgerReport

class LedgerReportAdmin(admin.ModelAdmin):
    list_display = ('date', 'sale_type', 'name', 'invoice_no', 'debit', 'credit', 'balance',)

admin.site.register(LedgerReport, LedgerReportAdmin)

