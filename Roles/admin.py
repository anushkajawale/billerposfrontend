from django.contrib import admin

from .models import Roles

# Register your models here.

class RolesAdmin(admin.ModelAdmin):
    list_display = ('Roles_id','Roles_name','Roles_slug')
admin.site.register(Roles,RolesAdmin)