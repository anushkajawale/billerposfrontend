from django.contrib import admin
from .models import Poschild
class PoschildAdmin(admin.ModelAdmin):
    list_display =('master_id','customer_id','product_id')
admin.site.register(Poschild,PoschildAdmin)

# Register your models here.
