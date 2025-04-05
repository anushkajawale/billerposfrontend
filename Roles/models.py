from django.db import models
from autoslug import AutoSlugField

class Roles(models.Model):
    id = models.AutoField(primary_key=True,unique=True) 

    Roles_name = models.CharField(max_length=255,unique=True)

    # Permissions
    Roles_Dashboard = models.BooleanField(default=False)
    Roles_UserProfile = models.BooleanField(default=False)
    Roles_BusinessProfile = models.BooleanField(default=False)
    Roles_BarcodePrint = models.BooleanField(default=False)
    Roles_Stock = models.BooleanField(default=False)
    Roles_HRDepartment = models.BooleanField(default=False)
    Roles_RewardPoint = models.BooleanField(default=False)

    # POS Permissions
    Roles_POS = models.BooleanField(default=False)
    Roles_POSList = models.BooleanField(default=False)
    Roles_POSCreate = models.BooleanField(default=False)
    Roles_POSUpdate = models.BooleanField(default=False)

    # Sales Permissions
    Roles_Sale = models.BooleanField(default=False)
    Roles_SaleList = models.BooleanField(default=False)
    Roles_SaleCreate = models.BooleanField(default=False)
    Roles_SaleUpdate = models.BooleanField(default=False)
    Roles_SaleDelete = models.BooleanField(default=False)

    # Purchase Permissions
    Roles_Purchase = models.BooleanField(default=False)
    Roles_PurchaseList = models.BooleanField(default=False)
    Roles_PurchaseCreate = models.BooleanField(default=False)
    Roles_PurchaseUpdate = models.BooleanField(default=False)
    Roles_PurchaseDelete = models.BooleanField(default=False)

    # Supplier Permissions
    Roles_Supplier = models.BooleanField(default=False)
    Roles_SupplierList = models.BooleanField(default=False)
    Roles_SupplierCreate = models.BooleanField(default=False)
    Roles_SupplierUpdate = models.BooleanField(default=False)
    Roles_SupplierDelete = models.BooleanField(default=False)

    # Settings
    Roles_Settings = models.BooleanField(default=False)
    Roles_Category = models.BooleanField(default=False)
    Roles_Brand = models.BooleanField(default=False)
    Roles_Taxes = models.BooleanField(default=False)
    Roles_Units = models.BooleanField(default=False)
    Roles_ExpensesTypes = models.BooleanField(default=False)
    Roles_PaymentModes = models.BooleanField(default=False)
    Roles_PaymentTerms = models.BooleanField(default=False)
    Roles_CustomerGroup = models.BooleanField(default=False)
    Roles_SupplierGroup = models.BooleanField(default=False)
    Roles_BarcodeSettings = models.BooleanField(default=False)
    Roles_PrinterSettings = models.BooleanField(default=False)
    Roles_BillingSettings = models.BooleanField(default=False)
    Roles_LanguageSettings = models.BooleanField(default=False)

    # Reports
    Roles_Reports = models.BooleanField(default=False)
    BillWiseProfit = models.BooleanField(default=False)
    Roles_OutStandingReport = models.BooleanField(default=False)
    Roles_LedgerReport = models.BooleanField(default=False)
    Roles_POSRegisterReport = models.BooleanField(default=False)

    # Customer Permissions
    Roles_Customer = models.BooleanField(default=False)
    Roles_CustomerList = models.BooleanField(default=False)
    Roles_CustomerCreate = models.BooleanField(default=False)
    Roles_CustomerUpdate = models.BooleanField(default=False)
    Roles_CustomerDelete = models.BooleanField(default=False)

    # Payments & User Management
    Roles_PaymentReceipt = models.BooleanField(default=False)
    Roles_Payment = models.BooleanField(default=False)
    Roles_UserManagement = models.BooleanField(default=False)
    Roles_Roles = models.BooleanField(default=False)
    Roles_User = models.BooleanField(default=False)

    # Product Permissions
    Roles_Product = models.BooleanField(default=False)
    Roles_ProductList = models.BooleanField(default=False)
    Roles_ProductCreate = models.BooleanField(default=False)
    Roles_ProductUpdate = models.BooleanField(default=False)
    Roles_ProductDelete = models.BooleanField(default=False)

    # Slug for URL-Friendly Names (Auto-generated)
    Roles_slug = AutoSlugField(populate_from='Roles_name', unique=True, always_update=True)

    class Meta:
        db_table = "tbl_Roles"

    def __str__(self):
        return self.Roles_name
