from django.contrib import admin

from .models import Users


# Register your models here.
class UsersAdmin(admin.ModelAdmin):
    list_display=('users_id','users_email','users_mobile','users_role','users_slug')
admin.site.register(Users, UsersAdmin)


 