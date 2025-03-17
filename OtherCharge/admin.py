from django.contrib import admin

from .models import OtherCharge


# Register your models here.
class otherchargeAdmin(admin.ModelAdmin):
    list_display=('othercharge_id','othercharge_name','othercharge_type','othercharge_amount')
admin.site.register(OtherCharge, otherchargeAdmin)

