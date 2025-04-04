from django.shortcuts import render,redirect,HttpResponse
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


from Employees.models import Employees

from Unit.models import Unit
from Expenses.models import Expenses
from OtherCharge.models import OtherCharge

from product.models import Product
from RewardPOints.models import RewardPoints









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

def insertpaymentmode (request):
    return render(request,"insertpaymentmode.html")

def login (request):
    return render(request,"login.html")


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

    except Brand.DoesNotExist:
        return JsonResponse({'error': 'Brand not found'}, status=404)       

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




    
from Unit.models import Unit
from Expenses.models import Expenses
from OtherCharge.models import OtherCharge
#########################################
def unitlist(request):
    list = Unit.objects.all()
    data = {
        "list":list
    }
    return render(request,'AddUnit.html',data)

def AddUnit(request):
    if request.method=='POST':
        unitname=request.POST.get('unitgroupname')

        insertunit=Unit(
            unit_name=unitname
        )

        insertunit.save()
        return redirect('/unit/')
    else:
        return render(request,'AddUnit.html')
    #########################

def expenseslist(request):
    list = Expenses.objects.all()
    data = {
        "list":list
    }
    return render(request,'AddExpenses.html',data)

def insertexpenses(request):
    if request.method=='POST':
        expensesname=request.POST.get('ExpensesName')

        insertexpenses=Expenses(
            expenses_name=expensesname
        )

        insertexpenses.save()
        return redirect('/AddExpenses/')
    else:
        return render(request,'AddExpenses.html')
    #########################
def chargelist(request):
    listdata = OtherCharge.objects.all()
    data = {
        "list":listdata
    }
    return render(request,'AddOtherCharge.html',data)

def insertcharge(request):
    if request.method=='POST':
        chargename=request.POST.get('chargename')
        


        insertcharge=OtherCharge(
            othercharge_name=chargename
        )
        insertcharge.save()
        return redirect('/AddOtherCharge/')
    else:
        return render(request,'AddOtherCharge.html')



#######################################


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
         return redirect("/Customergrouplist/")
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

 
def deleteCustomergroup(request,id):
    customergroupdata =Customergroup.objects.get(customergroup_id=id)
    customergroupdata.delete()
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
         return redirect("/Suppliergrouplist/")
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

def deleteSuppliergroup(request,id):
    suppliergroupdata =Suppliergroup.objects.get(suppliergroup_id=id)
    suppliergroupdata.delete()
    return redirect('/Suppliergrouplist/')          
    

def Paymenttermslist(request):
    listdata = Paymentterms.objects.all()
    data = {
        "list":listdata
    }
    return render(request,'Paymentterms.html',data)


def productslist(request):
    productdata=Product.objects.all()
    categorydata=Category.objects.all()
    branddata=Brand.objects.all()
    taxdata=Tax.objects.all()
    unitdata=Unit.objects.all()
    data={
        'categories':categorydata,
        'brands':branddata,
        'taxs':taxdata,
        'units':unitdata,
        'products':productdata
    }
    return render(request,'productlist.html',data)


def Employee(request):
    return render(request,'Employee.html')



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


def insertcustomer(request):
    if request.method=="POST":
        customer_name=request.POST.get("customer_name")
        customer_mobile=request.POST.get("customer_mobile")
        customer_email=request.POST.get("customer_email")
        customer_gstno=request.POST.get("customer_gstno")
        customer_panno=request.POST.get("customer_panno")
        customer_openingbal=request.POST.get("customer_openingbal")
        customer_grouptype=request.POST.get("customer_grouptype")
        customer_BillingAddress=request.POST.get("customer_BillingAddress")
        customer_ShippingAddress=request.POST.get("customer_ShippingAddress")
        customer_City=request.POST.get("customer_City")
        customer_CreditLimit=request.POST.get("customer_CreditLimit")
        customer_CreditPeriod=request.POST.get("customer_CreditPeriod")
        customer_barcode=request.POST.get("customer_barcode")
        




        insertquery=Customer(
           
        customer_name=customer_name,
        customer_mobile=customer_mobile,
        customer_email=customer_email,
        customer_gstno=customer_gstno,
        customer_panno=customer_panno,
        customer_openingbal=customer_openingbal,
        customer_grouptype=customer_grouptype,
        customer_BillingAddress=customer_BillingAddress,
        customer_ShippingAddress=customer_ShippingAddress,
        customer_City=customer_City,
        customer_CreditLimit=customer_CreditLimit,
        customer_CreditPeriod=customer_CreditPeriod,
        # customer_barcode=customer_barcode
       )
        
        insertquery.save()
        return redirect("/Customerpage/")
    else:
        return render(request,'customers.html')
        
       
    


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

def deleteCustomer(request,id):
    customerdata =Customer.objects.get(customer_id=id)
    customerdata.delete()
    return redirect('/Customerpage/')


def insertsupplier(request):
    if request.method=="POST":
        supplier_name=request.POST.get("supplier_name")
        supplier_mobile=request.POST.get("supplier_mobile")
        supplier_email=request.POST.get("supplier_email")
        supplier_gstno=request.POST.get("supplier_gstno")
        supplier_panno=request.POST.get("supplier_panno")
        supplier_openingbal=request.POST.get("supplier_openingbal")
        supplier_grouptype=request.POST.get("supplier_grouptype")
        supplier_BillingAddress=request.POST.get("supplier_BillingAddress")
        supplier_ShippingAddress=request.POST.get("supplier_ShippingAddress")
        supplier_City=request.POST.get("supplier_City")
        supplier_CreditLimit=request.POST.get("supplier_CreditLimit")
        supplier_CreditPeriod=request.POST.get("supplier_CreditPeriod")
        # supplier_barcode=request.POST.get("supplier_barcode")
        




        insertquery=Supplier(
           
        supplier_name=supplier_name,
        supplier_mobile=supplier_mobile,
        supplier_email=supplier_email,
        supplier_gstno=supplier_gstno,
        supplier_panno=supplier_panno,
        supplier_openingbal=supplier_openingbal,
        supplier_grouptype=supplier_grouptype,
        supplier_BillingAddress=supplier_BillingAddress,
        supplier_ShippingAddress=supplier_ShippingAddress,
        supplier_City=supplier_City,
        supplier_CreditLimit=supplier_CreditLimit,
        supplier_CreditPeriod=supplier_CreditPeriod,
        # customer_barcode=customer_barcode
       )
        
        insertquery.save()
        return redirect("/Supplierpage/")
    else:
        return render(request,'Suppliers.html')
    
def editsupplier(requset,id):
    try:
        supplierdata = Supplier.objects.get(supplier_id=id)
        edit = {
            'editsupplier': {
                'supplier_id': supplierdata.supplier_id,
                'supplier_name': supplierdata.supplier_name,  # Adjust field names based on your model
                'supplier_mobile': supplierdata.supplier_mobile,
                'supplier_email': supplierdata.supplier_email,
                'supplier_gstno': supplierdata.supplier_gstno,
                'supplier_panno': supplierdata.supplier_panno,
                'supplier_openingbal': supplierdata.supplier_openingbal,
                'supplier_grouptype': supplierdata.supplier_grouptype,
                'supplier_BillingAddress': supplierdata.supplier_BillingAddress,
                'supplier_ShippingAddress': supplierdata.supplier_ShippingAddress,
                'supplier_City': supplierdata.supplier_City,
                'supplier_CreditLimit': supplierdata.supplier_CreditLimit,
                # 'supplier_CreditPeriod': supplierdata.supplier_CreditPeriod
            }
        }
        return JsonResponse(edit)
    except Supplier.DoesNotExist:
        return JsonResponse({'error': 'Supplier not found'}, status=404)
    
def updatesupplier(request):
    if request.method =="POST":
        supplier_id=request.POST.get("supplier_id")
        supplier_name=request.POST.get("supplier_name") 
        supplier_mobile=request.POST.get("supplier_mobile") 
        supplier_email=request.POST.get("supplier_email") 
        supplier_gstno=request.POST.get("supplier_gstno") 
        supplier_panno=request.POST.get("supplier_panno") 
        supplier_openingbal=request.POST.get("supplier_openingbal") 
        supplier_grouptype=request.POST.get("supplier_grouptype'") 
        supplier_BillingAddress=request.POST.get("supplier_BillingAddress")
        supplier_ShippingAddress=request.POST.get("supplier_ShippingAddress")
        supplier_City=request.POST.get("supplier_City")
        supplier_CreditLimit=request.POST.get("supplier_CreditLimit")
        # supplier_CreditPeriod=request.POST.get("supplier_CreditPeriod")
       


         # Adjust field names based on your model

        
                
              
      
        

               
       

        fetchRecord=Supplier.objects.get(supplier_id=supplier_id)
        
        if supplier_name:
            fetchRecord.supplier_name=supplier_name
        if supplier_mobile:
            fetchRecord.supplier_mobile=supplier_mobile
        if  supplier_email:
            fetchRecord. supplier_email= supplier_email
        if supplier_gstno:
            fetchRecord.supplier_gstno=supplier_gstno
        if  supplier_panno:
            fetchRecord. supplier_panno= supplier_panno
        if supplier_openingbal:
            fetchRecord.supplier_openingbal=supplier_openingbal
        if supplier_grouptype:
            fetchRecord.supplier_grouptype=supplier_grouptype
        if supplier_BillingAddress:
            fetchRecord.supplier_BillingAddress=supplier_BillingAddress
        if  supplier_ShippingAddress:
            fetchRecord. supplier_ShippingAddress= supplier_ShippingAddress
        if supplier_City:
            fetchRecord.supplier_City=supplier_City
        if supplier_CreditLimit:
           fetchRecord.supplier_CreditLimit=supplier_CreditLimit
        # if supplier_CreditPeriod:
        #    fetchRecord.supplier_CreditPeriod
        

        
        
        
            

        fetchRecord.save()  
        return redirect('/Supplierpage/')  


def deleteSupplier(request,id):
    supplierdata =Supplier.objects.get(supplier_id=id)
    supplierdata.delete()
    return redirect('/Supplierpage/') 
     



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

def editAddUnit(request,id):
    
    try:
        unitdata = Unit.objects.get(unit_id=id)
        edit = {
            'editunit': {
                'unit_id': unitdata.unit_id,
                'unit_name': unitdata.unit_name,  # Adjust field names based on your model
            }
        }
        return JsonResponse(edit)
    except Unit.DoesNotExist:
        return JsonResponse({'error': 'Unit not found'}, status=404)





def updateunit(request):
    if request.method =="POST":
        unit_id=request.POST.get("unit_id")
        unit_name=request.POST.get("unit_name")  
        
        fetchRecord=Unit.objects.get(unit_id=unit_name)

        fetchRecord.unit_name=unit_name

        fetchRecord.save()  
        return redirect('/AddUnit/') 















    
def updateExpenses(request):
    if request.method =="POST":
        expenses_id=request.POST.get("expenses_id")
        expenses_name=request.POST.get("expenses_name")  
        

        fetchRecord=Expenses.objects.get(expenses_id=expenses_id)
        

        fetchRecord.expenses_name=expenses_name

        fetchRecord.save()  
        return redirect('/AddExpenses/')
    
def updateAddOtherCharge(request):
    if request.method =="POST":
        othercharge_id=request.POST.get("othercharge_id")
        othercharge_name=request.POST.get("othercharge_name")  
        

        fetchRecord=Expenses.objects.get(othercharge_id=othercharge_id)
        

        fetchRecord.othercharge_id=othercharge_id

        fetchRecord.save()  
        return redirect('/AddOtherCharge/')
    








def deleteunit(request,id):   
    unitdata=Unit.objects.get(unit_id=id)

    unitdata.delete()

    return redirect('/Unit/') 

def deleteexpenses(request,id):   
    expensesdata=Expenses.objects.get(expenses_id=id)

    expensesdata.delete()

    return redirect('/AddExpenses/')  

def deleteothercharge(request,id):   
    otherchargedata=OtherCharge.objects.get(othercharge_id=id)

    otherchargedata.delete()

    return redirect('/AddOtherCharge/')  

def RewardPointslist(request):

    RewardPointsdata = RewardPoints.objects.all() 

    data={
        "list":RewardPointsdata
    }   
    return render(request,'RewardPoints.html',data)

def insertrewardpoint(request):
    if request.method=="POST":
        RewardPoints_Minrange=request.POST.get("RewardPoints_Minrange")
        RewardPoints_Maxrange=request.POST.get("RewardPoints_Maxange")
        RewardPoints_Points=request.POST.get("RewardPoints_Points")
        
        
        insertquery=RewardPoints(
        RewardPoints_Minrange=RewardPoints_Minrange,
        RewardPoints_Maxrange=RewardPoints_Maxrange,
        RewardPoints_Points=RewardPoints_Points      # customer_barcode=customer_barcode
       )
        
        insertquery.save()
        return redirect("/RewardPoints/")
    else:
        return render(request,'RewardPoints.html')
    
def editrewardpointpage(request,id):
    try:
        RewardPointsdata = RewardPoints.objects.get(RewardPoints_id=id)
        edit = {
            'editrewardpoints': {
                'RewardPoints_id': RewardPointsdata.RewardPoints_id,
                'RewardPoints_Minrange': RewardPointsdata.RewardPoints_Minrange,
                'RewardPoints_Maxrange': RewardPointsdata. RewardPoints_Maxrange,
                'RewardPoints_Points':RewardPointsdata. RewardPoints_Points
                 
            }
        }
        return JsonResponse(edit)
    except RewardPoints.DoesNotExist:
        return JsonResponse({'error': ' not found'}, status=404)     
    





def Barcodepage(request):
    return render(request,'barcode.html')

def editproduct(request,id):
    try:
        productdata = Product.objects.get(product_id=id)
        edit = {
            'editproduct': {
                'product_id': productdata.product_id,
                'product_name': productdata.product_name, 
                'product_marathi_name': productdata.product_marathi_name, 
                'product_HSNCode':productdata.product_HSNCode,
                'category':{
                    'category_name':productdata.category.category_name},
                'brand':{
                    'brand_name':productdata.brand.brand_name},  
                'taxpercent':productdata.taxpercent,
                'tax':{
                    'tax_name':productdata.tax.tax_name},
                'unit':{
                    'unit_name':productdata.unit.unit_name},
                'alternateunit':productdata.alternateunit,
                'conversionfact':productdata.conversionfact,
                'nos':productdata.nos,                
                'barcode':productdata.barcode,                
                'qrcode':productdata.qrcode,                
                'mrp':productdata.mrp,                
                'sale':productdata.sale,                
                'credit':productdata.credit,                
                'purchase':productdata.purchase,                
                'wholesaler':productdata.wholesaler,                
                'distributor':productdata.distributor,                
                'purchase':productdata.purchase,                
                'op_Qty':productdata.op_Qty,                
                'op_Value':productdata.op_Value,                
                'mfg_Date':productdata.mfg_Date,                
                'exp_Date':productdata.exp_Date               
            }
        }
        return JsonResponse(edit)
    except Product.DoesNotExist:
        return JsonResponse({'error': ' Product not found'}, status=404) 
            
def stock(request):
    return render(request,'stock.html')

def Addsale(request):
    return render(request,'Addsale.html')


def Stock(request):
    return render(request,'stock.html')


def insertpaymentmode(request):
    if request.method=='POST':
        Paymentmode_name=request.POST.get('updatepaymentmode_name')

        insertpaymentmode=Paymentmode(
            Paymentmode_name=Paymentmode_name
        )

        insertpaymentmode.save()
        return redirect('/paymentmode/')
    else:
        return render(request,'paymentmode.html')
    


from django.shortcuts import get_object_or_404, redirect

def updatepaymentmode(request):
    if request.method == "POST":
        paymentmode_id = request.POST.get("updatepaymentmode_id")  # Ensure correct name
        paymentmode_name = request.POST.get("updatepaymentmode_name")  

        # Fetch record safely
        fetchRecord = get_object_or_404(Paymentmode, Paymentmode_id=paymentmode_id)

        # Update the record
        fetchRecord.Paymentmode_name = paymentmode_name
        fetchRecord.save()

        return redirect('/paymentmode/')  # Redirect back to the list page
    return redirect('/paymentmode/')  # Handle non-POST requests
    
def deletepaymentmode(request,id):   
    Paymentmodedata=Paymentmode.objects.get(Paymentmode_id=id)

    Paymentmodedata.delete()

    return redirect('/paymentmode/') 

def deletepaymentterms(request,id):   
    Paymenttermsdata=Paymentterms.objects.get(Paymentterms_id=id)

    Paymenttermsdata.delete()

    return redirect('/Paymentterms/') 

from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse


from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse

def updatepaymentterms(request, id):
    """Fetch and update payment terms."""
    paymentterms = get_object_or_404(Paymentterms, Paymentterms_id=id)

    if request.method == 'POST':
        new_name = request.POST.get('updatepaymentterms_name')
        if new_name:
            paymentterms.Paymentterms_name = new_name
            paymentterms.save()
            return redirect('/Paymentterms/')  # Redirect after successful update

    # If request is GET, return JSON data for the modal
    if request.method == 'GET':
        return JsonResponse({
            "Paymentterms_id": paymentterms.Paymentterms_id,
            "Paymentterms_name": paymentterms.Paymentterms_name
        })

def deleteproduct(request,id):
    productdata=Product.objects.get(product_id=id)


def BillWiselist(request):
    return render(request,'BillWiselist.html')

def OutstandingReport(request):
    return render(request,'OutstandingReport.html')


def POSRegisterReport(request):
    return render(request,'POSRegisterReport.html')

def insertpaymentterms(request):
    if request.method=='POST':
        Paymentterms_name=request.POST.get('updatepaymentterms_name')

        insertpaymentterms=Paymentterms(
            Paymentterms_name=Paymentterms_name
        )

        insertpaymentterms.save()
        return redirect('/Paymentterms/')
    else:
        return render(request,'Paymentterms.html')
    
from django.shortcuts import get_object_or_404, redirect
from django.http import HttpResponse
 # Ensure the model is imported

def updateuser(request):
    if request.method == "POST":
        users_id = request.POST.get("updateuser_id")
        if not users_id or not users_id.isdigit():
            return HttpResponse("Invalid User ID", status=400)  # Handle missing or invalid ID

        users_name = request.POST.get("updateuser_name")  
        users_email = request.POST.get("updateUser_email")
        users_mobile = request.POST.get("update_mob") 
        users_role = request.POST.get("update_role")
        users_pass = request.POST.get("update_pass")

        # Fetch record safely
        fetchRecord = get_object_or_404(Users, users_id=int(users_id))

        # Update fields if provided
        if users_mobile:
            fetchRecord.users_mobile = users_mobile
        if users_email:
            fetchRecord.users_email = users_email
        if users_role:
            fetchRecord.users_role = users_role
        if users_pass:
            fetchRecord.users_pass = users_pass

        fetchRecord.users_name = users_name  # Name should always update
        fetchRecord.save()

        return redirect('/Users/')  # Redirect to the user list
    return redirect('/Users/')  # Handle non-POST requests

def deleteusers(request,id):   
    Usersdata=Users.objects.get(users_id=id)

    Usersdata.delete()

    return redirect('/Users/') 


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

    

def adduser(request):
    if request.method=='POST':
        users_name=request.POST.get('updateuser_name')
        users_email=request.POST.get('updateUser_email')
        users_mobile=request.POST.get('update_mob')
        users_role=request.POST.get('update_role')
        users_pass=request.POST.get('update_pass')
        



        adduser=Users(
            users_name=users_name,
            users_email=users_email,
            users_mobile=users_mobile,
            users_role=users_role,
            users_pass=users_pass


        )


        adduser.save()
        return redirect('/Users/')
    else:
        return render(request,'Users.html')



def insertemployee(request):
    if request.method == "POST":
        Employees_firstname = request.POST.get("Employees_firstname")
        Employees_middlename = request.POST.get("Employees_middlename")
        Employees_lastname = request.POST.get("Employees_lastname")
        Employees_dateof_birth = request.POST.get("Employees_dateof_birth")
        Employees_gender = request.POST.get("Employees_gender")
        Employees_address = request.POST.get("Employees_address")
        Employees_mobile_number = request.POST.get("Employees_mobile_number")
        Employees_email = request.POST.get("Employees_email")

        Employees_highesteducation = request.POST.get("Employees_highesteducation")
        Employees_institutionsattended = request.POST.get("Employees_institutionsattended")
        Employees_degreesearned = request.POST.get("Employees_degreesearned")
        Employees_certifications = request.POST.get("Employees_certifications")

        Employees_vacationleave_balance = request.POST.get("Employees_vacationleave_balance")
        Employees_sickleave_balance = request.POST.get("Employees_sickleave_balance")
        Employees_leavetypes = request.POST.get("Employees_leavetypes")

        Employees_salary = request.POST.get("Employees_salary")
        Employees_payfrequency = request.POST.get("Employees_payfrequency")
        Employees_accountnumber = request.POST.get("Employees_accountnumber")
        Employees_ifsccode = request.POST.get("Employees_ifsccode")
        Employees_accountholder_name = request.POST.get("Employees_accountholder_name")

        employee_id = request.POST.get("employee_id")
        job_title = request.POST.get("job_title")
        department = request.POST.get("department")
        employment_status = request.POST.get("employment_status")
        hire_date = request.POST.get("hire_date")
        termination_date = request.POST.get("termination_date")

        Employees_emergencycontact_name = request.POST.get("Employees_emergencycontact_name")
        Employees_emergencycontact_relationship = request.POST.get("Employees_emergencycontact_relationship")
        Employees_emergencycontact_phone = request.POST.get("Employees_emergencycontact_phone")

        Employees_previous_employers = request.POST.get("Employees_previous_employers")
        Employees_previous_jobtitles = request.POST.get("Employees_previous_jobtitles")
        Employees_previous_responsibilities = request.POST.get("Employees_previous_responsibilities")

        Employees_resume = request.POST.get("Employees_resume")
        Employees_iddocument = request.POST.get("Employees_iddocument")
        Employees_certificationsdocument = request.POST.get("Employees_certificationsdocument")

        # Create a new Employee instance
        new_employee = Employees(
            Employees_firstname=Employees_firstname,
            Employees_middlename=Employees_middlename,
            Employees_lastname=Employees_lastname,
            Employees_dateof_birth=Employees_dateof_birth,
            Employees_gender=Employees_gender,
            Employees_address=Employees_address,
            Employees_mobile_number=Employees_mobile_number,
            Employees_email=Employees_email,

            Employees_highesteducation=Employees_highesteducation,
            Employees_institutionsattended=Employees_institutionsattended,
            Employees_degreesearned=Employees_degreesearned,
            Employees_certifications=Employees_certifications,

            Employees_vacationleave_balance=Employees_vacationleave_balance,
            Employees_sickleave_balance=Employees_sickleave_balance,
            Employees_leavetypes=Employees_leavetypes,

            Employees_salary=Employees_salary,
            Employees_payfrequency=Employees_payfrequency,
            Employees_accountnumber=Employees_accountnumber,
            Employees_ifsccode=Employees_ifsccode,
            Employees_accountholder_name=Employees_accountholder_name,

            employee_id=employee_id,
            job_title=job_title,
            department=department,
            employment_status=employment_status,
            hire_date=hire_date,
            termination_date=termination_date,

            Employees_emergencycontact_name=Employees_emergencycontact_name,
            Employees_emergencycontact_relationship=Employees_emergencycontact_relationship,
            Employees_emergencycontact_phone=Employees_emergencycontact_phone,

            Employees_previous_employers=Employees_previous_employers,
            Employees_previous_jobtitles=Employees_previous_jobtitles,
            Employees_previous_responsibilities=Employees_previous_responsibilities,

            Employees_resume=Employees_resume,
            Employees_iddocument=Employees_iddocument,
            Employees_certificationsdocument=Employees_certificationsdocument
        )

        new_employee.save()  # Save the employee data to the database

        return redirect("/Employees/")  # Redirect to the employees list page
    else:
        return render(request, 'Employees.html')  # Render the employee form page
    

           

    productdata.delete()
    return redirect("/products/")
 


