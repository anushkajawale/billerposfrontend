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

from Employees.models import Employees

from Unit.models import Unit
from Sales.models import Sales
from product.models import Product









def index (request):
    return render(request,"index.html")

def insertpaymentmode (request):
    return render(request,"insertpaymentmode.html")

def login (request):
    return render(request,"login.html")

def register (request):
    return render(request,"register.html")

def editemployee(request):
    return render(request,"editemployee.html")


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

def AddExpenses(request):
    if request.method=='POST':
        expensesname=request.POST.get('expensesgroupname')

        insertexpenses=AddExpenses(
            expenses_name=expensesname
        )

        insertexpenses.save()
        return redirect('/expenses/')
    else:
        return render(request,'AddExpenses.html')
    #########################

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
            fetchRecord.ustomergroup_id=customergroup_id
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
    listdata = Employees.objects.all()
    data = {
        "list":listdata
    }
    return render(request,'Employee.html',data)

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
     


    
    
        
       




from Unit.models import Unit




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


def edit(request):
    if request.method=="POST":
        Roles_id = request.POST.get('Roles_id')
        Roles_name=request.POST.get('Roles_name')
        Roles_dashboard=request.POST.get('Roles_dashboard')
    findRecord=Roles.objects.get(Roles_id = Roles_id)
    findRecord=Roles.objects.get(Roles_name = Roles_name)
    findRecord=Roles.objects.get(Roles_dashboard = Roles_dashboard)

    findRecord.save()
    return redirect("/EditRole/")

def EditRolelist(request):
    listdata= Roles.objects.all()   
    data = {
        'list':listdata
    }
    return render(request,'EditRole.html',data)

def add_role(request):
    if request.method == 'POST':
        role_name = request.POST.get('rolename')
        selected_permissions = request.POST.get('selected_permissions')  # Comma-separated values
        
        if role_name:
            role = role(name=role_name, permissions=selected_permissions)
            role.save()
            messages.success(request, "Role saved successfully!")
            return redirect('add_role')  # Reloads the same page after saving
        
        messages.error(request, "Role name is required!")
    
    return render(request, 'EditRole.html')

def role_list(request):
    Roles = Roles.objects.all()  # Fetch all roles
    return render(request, 'role_list.html', {'roles': Roles})

def edit_role(request):
    if request.method == "POST":
        role_name = request.POST.get("Rolename")
        
        # Check if the role exists, otherwise create a new one
        role = Roles.objects.get_or_create(name=role_name)

        # Update role permissions based on the checkboxes
        role.Role_Dashboard = request.POST.get("Role_Dashboard") == "True"
        role.Role_UserProfile = request.POST.get("Role_UserProfile") == "True"
        role.Role_BusinessProfile = request.POST.get("Role_BusinessProfile") == "True"

        # Save the role to the database
        role.save()

        return redirect("edit_role")  # Redirect back to the form after saving

    # If GET request, display the form
    roles = Roles.objects.all()
    return render(request, "your_template.html", {"list": roles})

def insertroles(request):
    if request.method=="POST":
        Roles_name=request.POST.get("role_name")
        Roles_Dashboard=request.POST.get("role_dashboard")
        Roles_UserProfile=request.POST.get("role_userprofile")
        Roles_BusinessProfile=request.POST.get("role_BusinessProfile")
        Roles_BarcodePrint=request.POST.get("role_BarcodePrint")
        Roles_Stock=request.POST.get("Roles_Stock")
        Roles_HRDepartment=request.POST.get("Roles_HRDepartment") 
        Roles_RewardPoint=request.POST.get("Roles_RewardPoint")
        Roles_POS=request.POST.get("Roles_POS")
        Roles_Sale=request.POST.get("Roles_Sale")
        Roles_Purchase=request.POST.get("Roles_Purchase")
        Roles_Supplier=request.POST.get("Roles_Supplier")
        Roles_Settings=request.POST.get("Roles_Settings")
        

        insertquery=Roles(
           Roles_name=Roles_name,
           Roles_Dashboard=Roles_Dashboard,
            Roles_UserProfile=Roles_UserProfile,
            Roles_BusinessProfile=Roles_BusinessProfile,
            Roles_BarcodePrint=Roles_BarcodePrint,
            Roles_Stock=Roles_Stock,
            Roles_HRDepartment=Roles_HRDepartment,
            Roles_RewardPoint=Roles_RewardPoint,
            Roles_POS=Roles_POS,
            Roles_Sale=Roles_Sale,
            Roles_Purchase=Roles_Purchase,
            Roles_Supplier=Roles_Supplier,
            Roles_Settings=Roles_Settings
        )

        
        
        insertquery.save()
        return redirect("/Roles/")
    else:
        return render(request,'Roles.html')
        

def Dashboard(request):
    
    return render(request, 'Dashboard.html') 

def POSBill (request):
    return render(request,'POSBills.html')

def Salelist (request):
    return render(request,'Salelist.html')






def updateunit(request):
    if request.method =="POST":
        unit_id=request.POST.get("unit_id")
        unit_name=request.POST.get("unitName")  
        

        fetchRecord=Category.objects.get(unit_id=unit_id)
        

        fetchRecord.category_name=unit_name

        fetchRecord.save()  
        return redirect('/unit/')
    
def deleteunit(request,id):   
    unitdata=Unit.objects.get(unit_id=id)

    unitdata.delete()

    return redirect('/unit/') 

def deleteexpenses(request,id):   
    expensesdata=Expenses.objects.get(expenses_id=id)

    expensesdata.delete()

    return redirect('/AddExpenses/')  

def deleteothercharge(request,id):   
    otherchargedata=OtherCharge.objects.get(othercharge_id=id)

    otherchargedata.delete()

    return redirect('/AddOtherCharge/')  

def RewardPoints(request):

    RewardPOintsdata = RewardPoints.objects.all() 

    data={
        "list":RewardPOintsdata
    }   
    return render(request,'RewardPoints.html',data)

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
        Paymentmode_name=request.POST.get('ipaymentmode_name')

        insertpaymentmode=Paymentmode(
            Paymentmode_name=Paymentmode_name
        )

        insertpaymentmode.save()
        return redirect('/paymentmode/')
    else:
        return render(request,'paymentmode.html')
    




def updatepaymentmode(request):
    if request.method == "POST":
        Paymentmode_id = request.POST.get("updatepaymentmode_id")  # Ensure correct name
        Paymentmode_name = request.POST.get("updatepaymentmode_name")  

        # Fetch record safely
        fetchRecord=Paymentmode.objects.get(Paymentmode_id=Paymentmode_id)

        # Update the record
        fetchRecord.Paymentmode_name = Paymentmode_name
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

        if not users_id:
            messages.error(request, "User ID missing from request.")
            return redirect('/Users/')

        try:
            fetchRecord = Users.objects.get(users_id=users_id)
            fetchRecord.users_name = request.POST.get("updateuser_name")
            fetchRecord.users_email = request.POST.get("updateuser_email")
            fetchRecord.users_mobile = request.POST.get("updatemob")
            fetchRecord.users_role = request.POST.get("updateRole")
            fetchRecord.users_pass = request.POST.get("update_pass")
            fetchRecord.save()
            messages.success(request, "User updated successfully.")
        except Users.DoesNotExist:
            messages.error(request, "User not found.")

        return redirect('/Users/')
    
    return redirect('/Users/')



def deleteusers(request,id):   
    Usersdata=Users.objects.get(users_id=id)

    Usersdata.delete()

    return redirect('/Users/') 


    

def adduser(request):
    if request.method == 'POST':
        users_name = request.POST.get('updateuser_name')
        users_email = request.POST.get('updateuser_email')
        users_mobile = request.POST.get('updatemob')
        users_role = request.POST.get('update_Role')  # ✅ fixed name here
        users_pass = request.POST.get('update_pass')

        adduser = Users(
            users_name=users_name,
            users_email=users_email,
            users_mobile=users_mobile,
            users_role=users_role,
            users_pass=users_pass
        )

        adduser.save()
        return redirect('/Users/')
    else:
        return render(request, 'Users.html')


from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import datetime


def insertemployee(request):
    if request.method == "POST":
        Employees_firstname = request.POST.get("first_name")
        Employees_middlename = request.POST.get("middle_name") 
        Employees_lastname = request.POST.get("last_name")
        Employees_dateof_birth = request.POST.get("date_birth")
        Employees_gender = request.POST.get("Gender")
        Employees_address = request.POST.get("address")
        Employees_mobile_number = request.POST.get("mob")
        Employees_email = request.POST.get("email_add")

        Employees_highesteducation = request.POST.get("high_education")
        Employees_institutionsattended = request.POST.get("institution_attended")
        Employees_degreesearned = request.POST.get("degrees_earned")
        Employees_certifications = request.POST.get("certifications")

        Employees_vacationleave_balance = request.POST.get("v_leave_balance")
        Employees_sickleave_balance = request.POST.get("s_leave_balance")
        Employees_leavetypes = request.POST.get("types_leave")

        Employees_salary = request.POST.get("salary")
        Employees_payfrequency = request.POST.get("pay_frequency")
        Employees_accountnumber = request.POST.get("acc_no")
        Employees_ifsccode = request.POST.get("ifsc_code")
        Employees_accountholder_name = request.POST.get("acc_holder")

        job_title = request.POST.get("job_title")
        department = request.POST.get("dept")
        employment_status = request.POST.get("emp_status")
        hire_date = request.POST.get("hire_date")
        termination_date = request.POST.get("termination_date")
        employee_id = request.POST.get("emp_id")

        Employees_emergencycontact_name = request.POST.get("e_name")
        Employees_emergencycontact_relationship = request.POST.get("relationship")
        Employees_emergencycontact_phone = request.POST.get("phone_no")

        Employees_previous_employers = request.POST.get("p_emp")
        Employees_previous_jobtitles = request.POST.get("job_titles")
        Employees_previous_responsibilities = request.POST.get("responsibilities")

        Employees_resume = request.FILES.get("resume")
        Employees_iddocument = request.FILES.get("id")
        Employees_certificationsdocument = request.FILES.get("d_certification")

        department_name = request.POST.get("d_name")
        department_birth = request.POST.get("d_birth")
        d_relationship = request.POST.get("d_relationship")

        

        # Convert date fields safely
        try:
            if Employees_dateof_birth:
                Employees_dateof_birth = datetime.strptime(Employees_dateof_birth, '%Y-%m-%d').date()
        except ValueError:
            Employees_dateof_birth = None

        try:
            if hire_date:
                hire_date = datetime.strptime(hire_date, '%Y-%m-%d').date()
        except ValueError:
            hire_date = None

        try:
            if termination_date:
                termination_date = datetime.strptime(termination_date, '%Y-%m-%d').date()
        except ValueError:
            termination_date = None

        # Convert department_birth safely
        try:
            if department_birth:
                department_birth = datetime.strptime(department_birth, '%Y-%m-%d').date()
        except ValueError:
            department_birth = None


        # Create new Employees instance
        insertemployee = Employees(
            Employees_firstname=Employees_firstname,
            Employees_middlename=Employees_middlename,
            Employees_lastname=Employees_lastname,
            Employees_dateof_birth=Employees_dateof_birth,
            Employees_gender=Employees_gender,
            Employees_address=Employees_address,
            Employees_mobile_number=Employees_mobile_number,
            Employees_email=Employees_email,
            employee_id = employee_id,

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
            Employees_certificationsdocument=Employees_certificationsdocument,

            department_name=department_name,
            department_birth=department_birth,
            d_relationship=d_relationship
        )

        insertemployee.save()

        return redirect("/Employee/")
    else:
        return render(request, 'Employee.html')
    
def addsale(request):
    if request.method == 'POST':
        # Collecting form data
        Sales_name = request.POST.get('Sales_name')
        invoice_no = request.POST.get('Sales_invoice_no')
        cash_sale = bool(request.POST.get('Sales_addcashsale'))
        credit_sale = bool(request.POST.get('Sales_add_creditsale'))
        cash = request.POST.get('Sales_addcash') or 0
        credit = request.POST.get('Sales_addcredit') or 0
        invoice_date = request.POST.get('Sales_addinvoicedate') 
        due_days = request.POST.get('Sales_add_duedays') or 0
        due_date = request.POST.get('Sales_add_duedate') or invoice_date
        product_name = request.POST.get('Sales_addproductname')
        qty = request.POST.get('Sales_qty') or 0
        payment_term = request.POST.get('Sales_payment_term')
        grand_total = request.POST.get('Sales_grand_total') or 0

        # Save to DB
        sale = Sales.objects.create(
            Sales_name=Sales_name,
            Sales_invoice_no=invoice_no,
            Sales_addcashsale=cash_sale,
            Sales_add_creditsale=credit_sale,
            Sales_addcash=cash,
            Sales_addcredit=credit,
            Sales_addinvoicedate=invoice_date,
            Sales_add_duedays=due_days,
            Sales_add_duedate=due_date,
            Sales_addproductname=product_name,
            Sales_qty=qty,
            Sales_payment_term=payment_term,
            Sales_grand_total=grand_total,
        )
        sale.save()

        messages.success(request, "Sale added successfully!")
        return redirect('/Sales/')

    return render(request, 'addsale.html')


# 👉 Sale List View
def salelist(request):
    sales = Sales.objects.all().order_by('-Sales_id')
    return render(request, 'sales/sale_list.html', {'sales': sales})
