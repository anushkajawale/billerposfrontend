from django.contrib import admin

from .models import Unit


# Register your models here.
class unitAdmin(admin.ModelAdmin):
    list_display=('unit_id','unit_name')
admin.site.register(Unit, unitAdmin)


 