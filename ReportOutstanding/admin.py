from django.contrib import admin
from .models import ReportOutstanding

class ReportOutstandingAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'customer_name', 'city','mobile','balance'
    )

admin.site.register(ReportOutstanding, ReportOutstandingAdmin)
# Register your models here.
