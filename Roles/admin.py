from django.contrib import admin
from .models import Roles

class RolesAdmin(admin.ModelAdmin):
    list_display = [
        'Roles_name', 'Roles_Dashboard', 'Roles_UserProfile', 'Roles_BusinessProfile',
        'Roles_BarcodePrint', 'Roles_Stock', 'Roles_HRDepartment', 'Roles_RewardPoint',
        'Roles_POS', 'Roles_POSList', 'Roles_POSCreate', 'Roles_POSUpdate',
        'Roles_Sale', 'Roles_SaleList', 'Roles_SaleCreate', 'Roles_SaleUpdate', 'Roles_SaleDelete',
        'Roles_Purchase', 'Roles_PurchaseList', 'Roles_PurchaseCreate', 'Roles_PurchaseUpdate', 'Roles_PurchaseDelete',
        'Roles_Supplier', 'Roles_SupplierList', 'Roles_SupplierCreate', 'Roles_SupplierUpdate', 'Roles_SupplierDelete',
        'Roles_Settings', 'Roles_Category', 'Roles_Brand', 'Roles_Taxes', 'Roles_Units',
        'Roles_ExpensesTypes', 'Roles_PaymentModes', 'Roles_PaymentTerms', 'Roles_CustomerGroup',
        'Roles_SupplierGroup', 'Roles_BarcodeSettings', 'Roles_PrinterSettings', 'Roles_BillingSettings',
        'Roles_LanguageSettings', 'Roles_Reports', 'BillWiseProfit', 'Roles_OutStandingReport',
        'Roles_LedgerReport', 'Roles_POSRegisterReport', 'Roles_Customer', 'Roles_CustomerList',
        'Roles_CustomerCreate', 'Roles_CustomerUpdate', 'Roles_CustomerDelete',
        'Roles_PaymentReceipt', 'Roles_Payment', 'Roles_UserManagement', 'Roles_Roles', 'Roles_User',
        'Roles_Product', 'Roles_ProductList', 'Roles_ProductCreate', 'Roles_ProductUpdate', 'Roles_ProductDelete',
        'Roles_slug'
    ]


admin.site.register(Roles, RolesAdmin)
