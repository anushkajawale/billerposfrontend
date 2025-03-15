from django.contrib import admin

from .models import Expenses


# Register your models here.
class expensesAdmin(admin.ModelAdmin):
    list_display=('expenses_id','expenses_name')
admin.site.register(Expenses, expensesAdmin)

