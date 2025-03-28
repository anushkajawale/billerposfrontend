from django.contrib import admin
from .models import Roles

class RolesAdmin(admin.ModelAdmin):
    list_display = [
        'Roles_name', 'Roles_Dashboard', 'Roles_UserProfile',
        'Roles_BusinessProfile', 'Roles_BarcodePrint', 'Roles_Stock',
        'Roles_HRDepartment', 'Roles_RewardPoint', 'Roles_POS',
        'Roles_Sale', 'Roles_Purchase', 'Roles_Supplier',
        'Roles_Settings', 'Roles_slug'
    ]

admin.site.register(Roles, RolesAdmin)
