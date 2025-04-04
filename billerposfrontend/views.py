from django.shortcuts import render,redirect
from Customergroup.models import Customergroup
from django.shortcuts import render
from django.http import JsonResponse
from Paymentmode.models import Paymentmode
from Paymentterms.models import Paymentterms
from category.models import Category
from brand.models import Brand
from Suppliergroup.models import Suppliergroup
from Roles.models import Roles

from django.contrib import messages
from django.db.models import Sum

from customer.models import Customer
from supplier.models import Supplier
from Users.models import Users
from tax.models import Tax
from django.contrib.auth import authenticate
from django.contrib.auth import logout as auth_logout









def index (request):
    return render(request,"index.html")



def login(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Login successful!")
            return redirect('dashboard')  # Change 'dashboard' to your actual home page
        else:
            messages.error(request, "Invalid email or password")

    return render(request, 'login.html')

def logout(request):  
    auth_logout(request)  
    messages.success(request, "Logged out successfully!")
    return redirect('login')  

def register (request):
    return render(request,"register.html")

def category(request):

    categorydata = Category.objects.all() 

    data={
        "list":categorydata
    }   
    return render(request,'category.html',data)

def editcategory(request, id):
    try:
        categorydata = Category.objects.get(category_id=id)
        edit = {
            'editcategory': {
                'category_id': categorydata.category_id,
                'category_name': categorydata.category_name,  # Adjust field names based on your model
                'category_img':  categorydata.category_img.url if categorydata.category_img else None,  # Adjust field names based on your model
                'category_bannerimg':   categorydata.category_bannerimg.url if categorydata.category_bannerimg else None,  
            }
        }
        return JsonResponse(edit)
    except Category.DoesNotExist:
        return JsonResponse({'error': 'Category not found'}, status=404)

    


def insertcategory(request):
    if request.method=="POST":
        category_name=request.POST.get("categoryName")
        category_img=request.FILES.get("categoryimg")
        category_bannerimg=request.FILES.get("categoryBanner")

        insertquery=Category(
           category_name=category_name,
           category_img=category_img,
           category_bannerimg=category_bannerimg
       )
        
        insertquery.save()
        return redirect("/category/")
    else:
        return render(request,'category.html')
        
def updatecategory(request):
    if request.method =="POST":
        category_id=request.POST.get("category_id")
        category_name=request.POST.get("categoryName")  
        category_img=request.FILES.get("categoryimg")
        category_bannerimg=request.FILES.get("categoryBanner") 

        fetchRecord=Category.objects.get(category_id=category_id)
        if category_img:
            fetchRecord.category_img=category_img
        if category_bannerimg:
            fetchRecord.category_bannerimg=category_bannerimg

        fetchRecord.category_name=category_name

        fetchRecord.save()  
        return redirect('/category/')


def deleteCategory(request,id):
    categorydata =Category.objects.get(category_id=id)
    categorydata.delete()
    return redirect('/category/')

    


     

def brand(request):
    branddata=Brand.objects.all()
    data={

        'branddata':branddata
    }

    return render(request,'brand.html',data)

def insertbrandpage(request):
    if request.method=='POST':
        brandname=request.POST.get('Brandname')
        brandImg=request.FILES.get('Brandimg')

        insertbrand=Brand(
            brand_name=brandname,
            brand_img=brandImg

        )
        insertbrand.save()
        return redirect('/brand/')
    else:
        return(request,'brand.html') 


def editbrand(request, id):
    try:
        branddata = Brand.objects.get(brand_id=id)
        edit = {
            'editbrand': {
                'brand_id': branddata.brand_id,
                'brand_name': branddata.brand_name,  # Adjust field names based on your model
                'brand_img':  branddata.brand_img.url if branddata.brand_img else None  # Adjust field names based on your model
  
            }
        }
        return JsonResponse(edit)
    except Brand.DoesNotExist:
        return JsonResponse({'error': ' Brand not found'}, status=404)       

    except Category.DoesNotExist:
        return JsonResponse({'error': ' not found'}, status=404)       



def updatebrand(request):       
    if request.method=='POST':
        brand_id=request.POST.get("brand_id")
        brand_name=request.POST.get("brandName")  
        brand_img=request.FILES.get("brandimg")

        fetchRecord=Brand.objects.get(brand_id=brand_id)
        fetchRecord.brand_name=brand_name
        if brand_img:
            fetchRecord.brand_img=brand_img
        
        fetchRecord.save()
        return redirect('/brand/')

def deleteBrand(requset,id):
    branddata =Brand.objects.get(brand_id=id)
    branddata.delete()
    return redirect('/brand/')

def AddUnit(request):
    return render(request,'AddUnit.html')

def AddExpenses(request):
    return render(request,'AddExpenses.html')

def AddOtherCharge(request):
    return render(request,'AddOtherCharge.html')

def Customergrouplist(request):
     customerData = Customergroup.objects.all()
     data ={
         "customer":customerData
     }      
     return render(request, 'Customergroup.html',data)



def insertcustomergroup(request):
    if request.method=='POST':
         customergroup=request.POST.get('customergroupname')

         insertquery=Customergroup(
         customergroup_name=customergroup
         )  

         insertquery.save() 
         return redirect("/Customerlist/")
    else:
        return render(request,'Customergroup.html') 
    
def editcustomergroup(request,id):
    try:
        customerdata = Customergroup.objects.get(customergroup_id=id)
        edit = {
            'editcustomergroup': {
                'customergroup_id': customerdata.customergroup_id,
                'customergroup_name': customerdata.customergroup_name,  # Adjust field names based on your model
                 
            }
        }
        return JsonResponse(edit)
    except Customergroup.DoesNotExist:
        return JsonResponse({'error': ' not found'}, status=404)
    
def updatecustomergroup(request):
    if request.method =="POST":
        customergroup_id=request.POST.get("customergroup_id")
        customergroup_name=request.POST.get("customergroupname")  
        

        fetchRecord=Customergroup.objects.get(customergroup_id=customergroup_id)
        if customergroup_id:
            fetchRecord.customergroup_id=customergroup_id
        if customergroup_name:
            fetchRecord.customergroup_name=customergroup_name

        fetchRecord.customergroup_name=customergroup_name

        fetchRecord.save()  
        return redirect('/Customergrouplist/')    



def Suppliergrouplist(request):
     supplierData = Suppliergroup.objects.all()
     data ={
         "supplier":supplierData
     }  
    
     return render(request, 'Supplierlist.html',data)

def insertsuppliergroup(request):
    if request.method=='POST':
         suppliergroup=request.POST.get('suppliergroupname')

         insertquery=Suppliergroup(
         suppliergroup_name=suppliergroup
         )  

         insertquery.save() 
         return redirect("/Supplierlist/")
    else:
        return render(request,'Supplier.html')
    
def editsuppliergroup(request,id):
    try:
        supplierdata = Suppliergroup.objects.get(suppliergroup_id=id)
        edit = {
            'editsuppliergroup': {
                'suppliergroup_id': supplierdata.suppliergroup_id,
                'suppliergroup_name': supplierdata.suppliergroup_name,  # Adjust field names based on your model
                 
            }
        }
        return JsonResponse(edit)
    except Suppliergroup.DoesNotExist:
        return JsonResponse({'error': ' not found'}, status=404)   
    
def updatesuppliergroup(request):
    if request.method =="POST":
        suppliergroup_id=request.POST.get("suppliergroup_id")
        suppliergroup_name=request.POST.get("suppliergroupname")  
        

        fetchRecord=Suppliergroup.objects.get(suppliergroup_id=suppliergroup_id)
        if suppliergroup_id:
            fetchRecord.suppliergroup_id=suppliergroup_id
        if suppliergroup_name:
            fetchRecord.suppliergroup_name=suppliergroup_name

        fetchRecord.suppliergroup_name=suppliergroup_name

        fetchRecord.save()  
        return redirect('/Suppliergrouplist/')      
    

 


def Paymenttermslist(request):
    listdata = Paymentterms.objects.all()
    data = {
        "list":listdata
    }
    return render(request,'Paymentterms.html',data)



def productslist(request):
    categorydata=Category.objects.all()
    branddata=Brand.objects.all()
    taxdata=Tax.objects.all()
    unitdata=Unit.objects.all()
    data={
        'categories':categorydata,
        'brands':branddata,
        'taxs':taxdata,
        'units':unitdata
    }
    return render(request,'productlist.html',data)
    


def Employee(request):
    return render(request,'Employee.html')

def RewardPoints(request):
    return render(request,'RewardPoints.html')

def Customerpage(request):
    customerdata=Customer.objects.all()
    data={
      'customer':customerdata
    }
    return render(request,'Customers.html',data)

def Supplierpage(request):
    supplierdata=Supplier.objects.all()
    data={
      'supplier':supplierdata
    }
    return render(request,'Suppliers.html',data)

def editcustomer(requset,id):
    try:
        customerdata = Customer.objects.get(customer_id=id)
        edit = {
            'editcustomer': {
                'customer_id': customerdata.customer_id,
                'customer_name': customerdata.customer_name,  # Adjust field names based on your model
                'customer_mobile': customerdata.customer_mobile,
                'customer_email': customerdata.customer_email,
                'customer_gstno': customerdata.customer_gstno,
                'customer_panno': customerdata.customer_panno,
                'customer_openingbal': customerdata.customer_openingbal,
                'customer_grouptype': customerdata.customer_grouptype,
                'customer_BillingAddress': customerdata.customer_BillingAddress,
                'customer_ShippingAddress': customerdata.customer_ShippingAddress,
                'customer_City': customerdata.customer_City,
                'customer_CreditLimit': customerdata.customer_CreditLimit,
                'customer_CreditPeriod': customerdata.customer_CreditPeriod
            }
        }
        return JsonResponse(edit)
    except Customer.DoesNotExist:
        return JsonResponse({'error': 'Customer not found'}, status=404)
    
def updatecustomer(request):
    if request.method =="POST":
        customer_id=request.POST.get("customer_id")
        customer_name=request.POST.get("customer_name") 
        customer_mobile=request.POST.get("customer_mobile") 
        customer_email=request.POST.get("customer_email") 
        customer_gstno=request.POST.get("customer_gstno") 
        customer_panno=request.POST.get("customer_panno") 
        customer_openingbal=request.POST.get("customer_openingbal") 
        customer_grouptype=request.POST.get("customer_grouptype'") 
        customer_BillingAddress=request.POST.get("customer_BillingAddress")
        customer_ShippingAddress=request.POST.get("customer_ShippingAddress")
        customer_City=request.POST.get("customer_City")
        customer_CreditLimit=request.POST.get("customer_CreditLimit")
        customer_CreditPeriod=request.POST.get("customer_CreditPeriod")
        customer_Barcode=request.POST.get("customer_Barcode")


         # Adjust field names based on your model

        
                
              
      
        

               
       

        fetchRecord=Customer.objects.get(customer_id=customer_id)
        
        if customer_name:
            fetchRecord.customer_name=customer_name
        if customer_mobile:
            fetchRecord.customer_mobile=customer_mobile
        if  customer_email:
            fetchRecord. customer_email= customer_email
        if customer_gstno:
            fetchRecord.customer_gstno=customer_gstno
        if  customer_panno:
            fetchRecord. customer_panno= customer_panno
        if customer_openingbal:
            fetchRecord.customer_openingbal=customer_openingbal
        if customer_grouptype:
            fetchRecord.customer_grouptype=customer_grouptype
        if customer_BillingAddress:
            fetchRecord.customer_BillingAddress=customer_BillingAddress
        if  customer_ShippingAddress:
            fetchRecord. customer_ShippingAddress= customer_ShippingAddress
        if customer_City:
            fetchRecord.customer_City=customer_City
        if customer_CreditLimit:
           fetchRecord.customer_CreditLimit=customer_CreditLimit
        if customer_CreditPeriod:
            fetchRecord.customer_CreditPeriod
        if customer_Barcode:
            fetchRecord.customer_Barcode=customer_Barcode

        
        
        
            

        fetchRecord.save()  
        return redirect('/Customerpage/')   




from Unit.models import Unit
def AddUnit(request):
    list = Unit.objects.all()
    data = {
        "list":list
    }
    return render(request,'AddUnit.html',data)



from Expenses.models import Expenses
def AddExpenses(request):
    list = Expenses.objects.all()
    data = {
        "list":list
    }
    return render(request,'AddExpenses.html',data)



from OtherCharge.models import OtherCharge
def AddOtherCharge(request):
    listdata = OtherCharge.objects.all()
    data = {
        "list":listdata
    }
    return render(request,'AddOtherCharge.html',data)

def paymentmodelist(request):
    listdata = Paymentmode.objects.all()
    data = {
        "list":listdata
    }
    return render(request,'paymentmode.html',data)

def Userslist(request):
    listdata = Users.objects.all()
    data = {
        "list":listdata
    }
    return render(request,'Users.html',data)




def POSBill(request):
    return render(request,'POSBills.html')

def printpage(request):
    return render(request,'printpage.html')


def Roleslist(request):
    listdata = Roles.objects.all()
    data = {
        'list':listdata
    }
    return render(request,'Roles.html',data)




    

def EditRolelist(request):
    listdata= Roles.objects.all()   
    data = {
        'list':listdata
    }
    return render(request,'EditRole.html',data)




def role_list(request):
    Roles = Roles.objects.all()  # Fetch all roles
    return render(request, 'role_list.html')

def EditRoles(request):
    if request.method == "POST":
        id = request.POST.get("id")
        Roles_name = request.POST.get("Rolesname")

      
        fetchRecord = Roles.objects.get(id=id)

        if Roles_name:
            fetchRecord.Roles_name = request.POST.get('Rolesname', False)
            fetchRecord.Roles_Dashboard = request.POST.get('RolesDashboard', False)
            fetchRecord.Roles_UserProfile = request.POST.get('RolesUserProfile', False)
            fetchRecord.Roles_BusinessProfile = request.POST.get('RolesBusinessProfile', False)
            fetchRecord.Roles_BarcodePrint = request.POST.get('RolesBarcodePrint', False)
            fetchRecord.Roles_Stock = request.POST.get('RolesStock', False)
            fetchRecord.Roles_HRDepartment = request.POST.get('RolesHRDepartment', False)
            fetchRecord.Roles_RewardPoint = request.POST.get('RolesRewardPoint', False)
            fetchRecord.Roles_POS = request.POST.get('RolesPOS', False)
            fetchRecord.Roles_POSList = request.POST.get('RolesPOSList', False)
            fetchRecord.Roles_POSCreate = request.POST.get('RolesPOSCreate', False)
            fetchRecord.Roles_POSUpdate = request.POST.get('RolesPOSUpdate', False)
            fetchRecord.Roles_Sale = request.POST.get('RolesSale', False)
            fetchRecord.Roles_SaleList = request.POST.get('RolesSaleList', False)
            fetchRecord.Roles_SaleCreate = request.POST.get('RolesSaleCreate', False)
            fetchRecord.Roles_SaleUpdate = request.POST.get('RolesSaleUpdate', False)
            fetchRecord.Roles_SaleDelete = request.POST.get('RolesSaleDelete', False)
            fetchRecord.Roles_Purchase = request.POST.get('RolesPurchase', False)
            fetchRecord.Roles_PurchaseList = request.POST.get('RolesPurchaseList', False)
            fetchRecord.Roles_PurchaseCreate = request.POST.get('RolesPurchaseCreate', False)
            fetchRecord.Roles_PurchaseUpdate = request.POST.get('RolesPurchaseUpdate', False)
            fetchRecord.Roles_PurchaseDelete = request.POST.get('Roles_PurchaseDelete', False)
            fetchRecord.Roles_Supplier = request.POST.get('Roles_Supplier', False)
            fetchRecord.Roles_SupplierList = request.POST.get('Roles_SupplierList', False)
            fetchRecord.Roles_SupplierCreate = request.POST.get('RolesSupplierCreate', False)
            fetchRecord.Roles_SupplierUpdate = request.POST.get('RolesSupplierUpdate', False)
            fetchRecord.Roles_SupplierDelete = request.POST.get('RolesSupplierDelete', False)
            fetchRecord.Roles_Settings = request.POST.get('RolesSettings', False)
            fetchRecord.Roles_Category = request.POST.get('RolesCategory', False)
            fetchRecord.Roles_Brand = request.POST.get('RolesBrand', False)
            fetchRecord.Roles_Taxes = request.POST.get('RolesTaxes', False)
            fetchRecord.Roles_Units = request.POST.get('RolesUnits', False)
            fetchRecord.Roles_ExpensesTypes = request.POST.get('RolesExpensesTypes', False)
            fetchRecord.Roles_PaymentModes = request.POST.get('RolesPaymentModes', False)
            fetchRecord.Roles_PaymentTerms = request.POST.get('RolesPaymentTerms', False)
            fetchRecord.Roles_CustomerGroup = request.POST.get('RolesCustomerGroup', False)
            fetchRecord.Roles_SupplierGroup = request.POST.get('RolesSupplierGroup', False)
            fetchRecord.Roles_BarcodeSettings = request.POST.get('RolesBarcodeSettings', False)
            fetchRecord.Roles_PrinterSettings = request.POST.get('RolesPrinterSettings', False)
            fetchRecord.Roles_BillingSettings = request.POST.get('RolesBillingSettings', False)
            fetchRecord.Roles_LanguageSettings = request.POST.get('RolesLanguageSettings', False)
            fetchRecord.Roles_Reports = request.POST.get('RolesReports', False)
            fetchRecord.BillWiseProfit = request.POST.get('BillWiseProfit', False)
            fetchRecord.Roles_OutStandingReport = request.POST.get('RolesOutStandingReport', False)
            fetchRecord.Roles_LedgerReport = request.POST.get('RolesLedgerReport', False)
            fetchRecord.Roles_POSRegisterReport = request.POST.get('RolesPOSRegisterReport', False)
            fetchRecord.Roles_Customer = request.POST.get('RolesCustomer', False)
            fetchRecord.Roles_CustomerList = request.POST.get('RolesCustomerList', False)
            fetchRecord.Roles_CustomerCreate = request.POST.get('RolesCustomerCreate', False)
            fetchRecord.Roles_CustomerUpdate = request.POST.get('RolesCustomerUpdate', False)
            fetchRecord.Roles_CustomerDelete = request.POST.get('RolesCustomerDelete', False)
            fetchRecord.Roles_PaymentReceipt = request.POST.get('RolesPaymentReceipt', False)
            fetchRecord.Roles_Payment = request.POST.get('RolesPayment', False)
            fetchRecord.Roles_UserManagement = request.POST.get('RolesUserManagement', False)
            fetchRecord.Roles_Roles = request.POST.get('RolesRoles', False)
            fetchRecord.Roles_User = request.POST.get('RolesUser', False)
            fetchRecord.Roles_Product = request.POST.get('RolesProduct', False)
            fetchRecord.Roles_ProductList = request.POST.get('Roles_ProductList', False)
            fetchRecord.Roles_ProductCreate = request.POST.get('RolesProductCreate', False)
            fetchRecord.Roles_ProductUpdate = request.POST.get('RolesProductUpdate', False)
            fetchRecord.Roles_ProductDelete = request.POST.get('RolesProductDelete', False)

        
        fetchRecord.save()

        return redirect("/Roles/")
    return render(request, "EditRole.html")
  
   

def insertroles(request):
    if request.method=="POST":
        insert_query = Roles(
            id=request.POST.get('Roles_id',False),
            Roles_name=request.POST.get('Roles_name',False),
            Roles_Dashboard=request.POST.get('RolesDashboard', False),
            Roles_UserProfile=request.POST.get('RolesUserProfile', False),
            Roles_BusinessProfile=request.POST.get('RolesBusinessProfile', False),
            Roles_BarcodePrint=request.POST.get('RolesBarcodePrint', False),
            Roles_Stock=request.POST.get('RolesStock', False),
            Roles_HRDepartment=request.POST.get('RolesHRDepartment', False),
            Roles_RewardPoint=request.POST.get('RolesRewardPoint', False),
            Roles_POS=request.POST.get('RolesPOS', False),
            Roles_POSList=request.POST.get('RolesPOSList', False),
            Roles_POSCreate=request.POST.get('RolesPOSCreate',False),
            Roles_POSUpdate=request.POST.get('RolesPOSUpdate', False),
            Roles_Sale=request.POST.get('RolesSale', False),
            Roles_SaleList=request.POST.get('RolesSaleList', False),
            Roles_SaleCreate=request.POST.get('RolesSaleCreate', False),
            Roles_SaleUpdate=request.POST.get('RolesSaleUpdate', False),
            Roles_SaleDelete=request.POST.get('RolesSaleDelete', False),
            Roles_Purchase=request.POST.get('RolesPurchase', False),
            Roles_PurchaseList=request.POST.get('Roles_PurchaseList', False),
            Roles_PurchaseCreate=request.POST.get('Roles_PurchaseCreate', False),
            Roles_PurchaseUpdate=request.POST.get('Roles_PurchaseUpdate', False),
            Roles_PurchaseDelete=request.POST.get('Roles_PurchaseDelete', False),
            Roles_Supplier=request.POST.get('Roles_Supplier', False),
            Roles_SupplierList=request.POST.get('Roles_SupplierList', False),
            Roles_SupplierCreate=request.POST.get('Roles_SupplierCreate', False),
            Roles_SupplierUpdate=request.POST.get('Roles_SupplierUpdate', False),
            Roles_SupplierDelete=request.POST.get('Roles_SupplierDelete', False),
            Roles_Settings=request.POST.get('Roles_Settings', False),
            Roles_Category=request.POST.get('Roles_Category', False),
            Roles_Brand=request.POST.get('Roles_Brand', False),
            Roles_Taxes=request.POST.get('Roles_Taxes', False),
            Roles_Units=request.POST.get('Roles_Units', False),
            Roles_ExpensesTypes=request.POST.get('Roles_ExpensesTypes', False),
            Roles_PaymentModes=request.POST.get('Roles_PaymentModes', False),
            Roles_PaymentTerms=request.POST.get('Roles_PaymentTerms', False),
            Roles_CustomerGroup=request.POST.get('Roles_CustomerGroup', False),
            Roles_SupplierGroup=request.POST.get('Roles_SupplierGroup', False),
            Roles_BarcodeSettings=request.POST.get('Roles_BarcodeSettings', False),
            Roles_PrinterSettings=request.POST.get('Roles_PrinterSettings', False),
            Roles_BillingSettings=request.POST.get('Roles_BillingSettings', False),
            Roles_LanguageSettings=request.POST.get('Roles_LanguageSettings', False),
            Roles_Reports=request.POST.get('Roles_Reports', False),
            BillWiseProfit=request.POST.get('BillWiseProfit', False),
            Roles_OutStandingReport=request.POST.get('Roles_OutStandingReport', False),
            Roles_LedgerReport=request.POST.get('Roles_LedgerReport', False),
            Roles_POSRegisterReport=request.POST.get('Roles_POSRegisterReport', False),
            Roles_Customer=request.POST.get('Roles_Customer', False),
            Roles_CustomerList=request.POST.get('Roles_CustomerList', False),
            Roles_CustomerCreate=request.POST.get('Roles_CustomerCreate', False),
            Roles_CustomerUpdate=request.POST.get('Roles_CustomerUpdate', False),
            Roles_CustomerDelete=request.POST.get('Roles_CustomerDelete', False),
            Roles_PaymentReceipt=request.POST.get('Roles_PaymentReceipt', False),
            Roles_Payment=request.POST.get('Roles_Payment', False),
            Roles_UserManagement=request.POST.get('Roles_UserManagement', False),
            Roles_Roles=request.POST.get('Roles_Roles', False),
            Roles_User=request.POST.get('Roles_User', False),
            Roles_Product=request.POST.get('Roles_Product', False),
            Roles_ProductList=request.POST.get('Roles_ProductList', False),
            Roles_ProductCreate=request.POST.get('RolesProductCreate', False),
            Roles_ProductUpdate=request.POST.get('RolesProductUpdate', False),
            Roles_ProductDelete=request.POST.get('RolesProductDelete', False)
        )

        insert_query.save()
        messages.success(request, "Role successfully added!")
        return redirect('/Roles/')  #

    return render(request, "insertroles.html")


        

        
    

def Dashboard(request):
    
    return render(request, 'Dashboard.html') 

def POSBill (request):
    return render(request,'POSBills.html')

def Salelist (request):
    return render(request,'Salelist.html')

def Salelist (request):
    return render(request,'Salelist.html')




def updateunit(request):
    if request.method =="POST":
        unit_id=request.POST.get("unit_id")
        unit_name=request.POST.get("unitName")  
        

        fetchRecord=Category.objects.get(unit_id=unit_id)
        

        fetchRecord.category_name=unit_name

        fetchRecord.save()  
        return redirect('/AddUnit/')
    
def deleteunit(request,id):   
    unitdata=Unit.objects.get(unit_id=id)

    unitdata.delete()

    return redirect('/AddUnit/') 

def deleteexpenses(request,id):   
    expensesdata=Expenses.objects.get(expenses_id=id)

    expensesdata.delete()

    return redirect('/AddExpenses/')  

def deleteothercharge(request,id):   
    otherchargedata=OtherCharge.objects.get(othercharge_id=id)

    otherchargedata.delete()

    return redirect('/AddOtherCharge/')  

def Barcodepage(request):
    return render(request,'barcode.html')


def stock(request):
    return render(request,'stock.html')

def Addsale(request):
    return render(request,'Addsale.html')


def Stock(request):
    return render(request,'stock.html')

def BillWiselist(request):
    return render(request,'BillWiselist.html')

def OutstandingReport(request):
    return render(request,'OutstandingReport.html')

def POSRegisterReport(request):
    return render(request,'POSRegisterReport.html')

def LedgerReport(request):
    return render(request,'LedgerReport.html')

def POSRegistrationReport(request):
    return render(request,'POSRegistrationReport.html')

def PrintLedgerReport(request):
    return render(request,'PrintLedgerReport.html')

def PrintOutStandingReport(request):
    return render(request,'PrintOutStandingReport.html')
   
def  PrintPOSRegisterReport(request):
    return render(request,'PrintPOSRegisterReport.html')
   
def  PrintBillWiseReport(request):
    return render(request,'PrintBillWiseReport.html')