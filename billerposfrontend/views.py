
from django.shortcuts import render,redirect,HttpResponse,get_list_or_404

from django.shortcuts import render,redirect,HttpResponse,get_object_or_404

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
from master.models import Master
from poschild.models import Poschild


from Employees.models import Employees

from Unit.models import Unit

from Sales.models import Sales


from Expenses.models import Expenses
from OtherCharge.models import OtherCharge


from product.models import Product
from RewardPOints.models import RewardPoints











def index (request):
    return render(request,"index.html")


def Dashboard(request):
    if 'user_id' not in request.session:
        return redirect('login')

    total_bills = Poschild.objects.count()
    total_products = Product.objects.count()
    total_customers = Customer.objects.count()
    # total_receipts = Receipt.objects.count() 

    context = {
        'total_bills': total_bills,
        'total_products': total_products,
        'total_customers': total_customers,
    
    }
    return render(request, 'Dashboard.html')



           
       
#session


def login(request):
    error_message = ""
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
         
        try:
            Employee = Employees.objects.get(Employees_email=email, Employees_mobile_number=password)


            request.session['user_name'] = email
         

            request.session['user_id'] = str(Employees.Employees_id)
            print(f"DEBUG: Employee ID from session: {request.session.get('Employees_id')}")
  

            return redirect("/Dashboard/")  
        except Employees.DoesNotExist:
            error_message = "Invalid email or password. Please try again."
    
    return render(request, 'login.html', {"error": error_message})


def logout(request):  
    if 'username' in request.session:
        del request.session['username']
        return redirect("/login/")

     

def insertpaymentmode (request):
    return render(request,"insertpaymentmode.html")






def register (request):
    return render(request,"register.html")

def editEmployeeModal(request,id):
    try:

        employeedata = Employees.objects.get(Employees_id=id)
        edit = {
            'editemployee' : {
                'Employee_id':employeedata.Employees_id,
                'Employees_firstname':employeedata.Employees_firstname,
                'Employees_middlename':employeedata.Employees_middlename,
                'Employees_lastname':employeedata.Employees_lastname,
                'Employees_dateof_birth':employeedata.Employees_dateof_birth,
                'Employees_gender': employeedata.Employees_gender,
                'Employees_address':employeedata.Employees_address,
                'Employees_mobile_number':employeedata.Employees_mobile_number,
                'Employees_email':employeedata.Employees_email,
                'Employees_highesteducation':employeedata.Employees_highesteducation,
                'Employees_institutionsattended':employeedata.Employees_institutionsattended,
                'Employees_degreesearned':employeedata.Employees_degreesearned,
                'Employees_certifications':employeedata.Employees_certifications,
                'Employees_vacationleave_balance':employeedata.Employees_vacationleave_balance,
                'Employees_sickleave_balance':employeedata.Employees_sickleave_balance,
                'Employees_leavetypes':employeedata.Employees_leavetypes,
                'Employees_salary':employeedata.Employees_salary,
                'Employees_payfrequency':employeedata.Employees_payfrequency,
                'Employees_accountnumber':employeedata.Employees_accountnumber,
                'Employees_ifsccode':employeedata.Employees_ifsccode,
                'Employees_accountholder_name':employeedata.Employees_accountholder_name,
                'department':employeedata.department,
                'employment_status':employeedata.employment_status,
                'hire_dat':employeedata.hire_date,
                'termination_date':employeedata.termination_date,
                'Employees_emergencycontact_name':employeedata.Employees_emergencycontact_name,
                'Employees_emergencycontact_relationship':employeedata.Employees_emergencycontact_relationship,
                'Employees_emergencycontact_phone':employeedata.Employees_emergencycontact_phone,
                'Employees_previous_employers' :employeedata.Employees_previous_employers,
                'Employees_previous_jobtitles' :employeedata.Employees_previous_jobtitles,
                'Employees_previous_responsibilities': employeedata.Employees_previous_responsibilities,
                'department_name' : employeedata.department_name,
                'department_birth' : employeedata.department_birth,
                'Employees_resume' : employeedata.Employees_resume.url if employeedata.Employees_resume else None,
                'Employees_iddocument': employeedata.Employees_iddocument.url if employeedata.Employees_iddocument else None,
                'd_relationship': employeedata.d_relationship
            }
        }
        return JsonResponse(edit)
    except Employees.DoesNotExist:
        return JsonResponse({'error': 'Employee not found'}, status=404)



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
    paymenttermsdata = Paymentterms.objects.all()
    data = {
        "paymenttermsdata":paymenttermsdata
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
    employeedata = Employees.objects.all()
    data = {
        "employeedata":employeedata
    }
    return render(request,'Employee.html',data)



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
            fetchRecord.customer_CreditPeriod=customer_CreditPeriod
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
        supplier_CreditPeriod=supplier_CreditPeriod

        
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
                'supplier_name': supplierdata.supplier_name, 
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
                'supplier_CreditPeriod': supplierdata.supplier_CreditPeriod,
                
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
        supplier_CreditPeriod=request.POST.get("supplier_CreditPeriod")
        
       


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
        if supplier_CreditPeriod:
            fetchRecord.supplier_CreditPeriod=supplier_CreditPeriod

       
        

        
        
        
            

        fetchRecord.save()  
        return redirect('/Supplierpage/')  


def deleteSupplier(request,id):
    supplierdata =Supplier.objects.get(supplier_id=id)
    supplierdata.delete()
    return redirect('/Supplierpage/') 
     



def paymentmodelist(request):
    paymentmodedata=Paymentmode.objects.all()
    data={

        'paymentmodedata':paymentmodedata
    }
    return render(request,'paymentmode.html',data)

def Userslist(request):
    usersdata = Users.objects.all()
    data = {
        "usersdata":usersdata
    }
    return render(request,'Users.html',data)



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


def updateroles(request):
    if request.method == "POST":
        id=request.POST.get('id')
        Roles_name = request.POST.get("Roles_name")

        if Roles_name:
            fetchRecord = Roles.objects.get(id=id)
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
    

def EditRoles(request,id):
       try:
            rolesdata=Roles.objects.get(id=id)
            data= {
                    'id': rolesdata.id,
                    'Roles_name': rolesdata.Roles_name,
                    'Dashboard':rolesdata.Roles_Dashboard,
                    'UserProfile':rolesdata.Roles_UserProfile,
                    'BusinessProfile':rolesdata.Roles_BusinessProfile,
                    'HRDepartment':rolesdata.Roles_HRDepartment,
                    'Stock':rolesdata.Roles_Stock,
                    'BarcodePrint':rolesdata.Roles_BarcodePrint,
                    'POS':rolesdata.Roles_POS,
                    'Sale':rolesdata.Roles_Sale,
                    'Purchase':rolesdata.Roles_Purchase,
                    'RewardPoint':rolesdata.Roles_RewardPoint,
                    'Supplier':rolesdata.Roles_Supplier,
                    'POSList':rolesdata.Roles_POSList,
                    'POSCreate':rolesdata.Roles_POSCreate,
                    'Sale':rolesdata.Roles_Sale,
                    'SaleList':rolesdata.Roles_SaleList,
                    'SaleCreate':rolesdata.Roles_SaleCreate,
                    'SaleUpdate':rolesdata.Roles_SaleUpdate,
                    'SaleDelete':rolesdata.Roles_SaleDelete,
                    'Purchase':rolesdata.Roles_Purchase,
                    'PurchaseList':rolesdata.Roles_PurchaseList,
                    'PurchaseCreate':rolesdata.Roles_PurchaseCreate,
                    'PurchaseUpdate':rolesdata.Roles_PurchaseUpdate,
                    'PurchaseDelete':rolesdata.Roles_PurchaseDelete,
                    'Supplier':rolesdata.Roles_Supplier,
                    'SupplierList':rolesdata.Roles_SupplierList,
                    'SupplierCreate':rolesdata.Roles_SupplierCreate,
                    'SupplierUpdate':rolesdata.Roles_SupplierUpdate,
                    'SupplierDelete':rolesdata.Roles_SupplierDelete,
                    'Settings':rolesdata.Roles_Settings,
                    'Category':rolesdata.Roles_Category,
                    'Brand':rolesdata.Roles_Brand,
                    'Taxes':rolesdata.Roles_Taxes,
                    'Units':rolesdata.Roles_Units,
                    'ExpensesTypes':rolesdata.Roles_ExpensesTypes,
                    'PaymentModes':rolesdata.Roles_PaymentModes,
                    'PaymentTerms':rolesdata.Roles_PaymentTerms,
                    'CustomerGroup':rolesdata.Roles_CustomerGroup,
                    'SupplierGroup':rolesdata.Roles_SupplierGroup,
                    'BarcodeSettings':rolesdata.Roles_BarcodeSettings,
                    'PrinterSettings':rolesdata.Roles_PrinterSettings,
                    'BillingSettings':rolesdata.Roles_BillingSettings,
                    'LanguageSettings':rolesdata.Roles_LanguageSettings,
                    'Reports':rolesdata.Roles_Reports,
                    'BillWiseProfit':rolesdata.BillWiseProfit,
                    'OutStandingReports':rolesdata.Roles_OutStandingReport,
                    'LedgerReports':rolesdata.Roles_LedgerReport,
                    'POSRegisterReports':rolesdata.Roles_POSRegisterReport,
                    'Customer':rolesdata.Roles_Customer,
                    'CustomerList ':rolesdata.Roles_CustomerList, 
                    'CustomerCreate ':rolesdata.Roles_CustomerCreate, 
                    'CustomerUpdate ':rolesdata.Roles_CustomerUpdate, 
                    'CustomerDelete ':rolesdata.Roles_CustomerDelete,
                    'PaymentReciept ':rolesdata.Roles_PaymentReceipt,
                    'UserManagement':rolesdata.Roles_UserManagement ,
                    'Roles':rolesdata.Roles_Roles ,
                    'User':rolesdata.Roles_User ,
                    'Product':rolesdata.Roles_Product ,
                    'ProductList':rolesdata.Roles_ProductList ,
                    'ProductCreate':rolesdata.Roles_ProductCreate,
                    'ProductUpdate':rolesdata.Roles_ProductUpdate,
                    'ProductDelete':rolesdata.Roles_ProductDelete,
                }
            return render(request, "EditRole.html",data)
       except Roles.DoesNotExist:
        return HttpResponse("Role not found", status=404)
 

    
def insertroles(request):
    if request.method=="POST":
        insert_query = Roles( 
            Roles_name=request.POST.get('Roles_name'),
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



def deleteRoles(request,id):
    rolesdata =Roles.objects.get(id=id)
    rolesdata.delete()
    return redirect('/Roles/') 
     


def POSBill (request):
    return render(request,'POSBills.html')

def Salelist(request):
    saledata=Sales.objects.all()
    data={

        'saledata':saledata
    }
    return render(request,'salelist.html',data)

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
        
        fetchRecord=Unit.objects.get(unit_id=unit_id)

        fetchRecord.unit_name=unit_name

        fetchRecord.save()  
        return redirect('/unit/') 


def editAddExpenses(request,id):
    
    try:
        expensesdata = Expenses.objects.get(expenses_id=id)
        edit = {
            'editexpenses': {
                'expenses_id': expensesdata.expenses_id,
                'expenses_name': expensesdata.expenses_name,  # Adjust field names based on your model
            }
        }
        return JsonResponse(edit)
    except Expenses.DoesNotExist:
        return JsonResponse({'error': 'Expenses not found'}, status=404)


def updateexpenses(request):
    if request.method =="POST":
        expenses_name=request.POST.get("ExpensesName")
        expenses_id=request.POST.get("updateExpenses_id")  
        
        fetchRecord=Expenses.objects.get(expenses_id=expenses_id)

        fetchRecord.expenses_name=expenses_name

        fetchRecord.save()  
        return redirect('/AddExpenses/') 


def editAddOtherCharge(request,id):
    
    try:
        expensesdata = OtherCharge.objects.get(othercharge_id=id)
        edit = {
            'editAddOtherCharge': {
                'othercharge_id': expensesdata.othercharge_id,
                'othercharge_name': expensesdata.othercharge_name,  # Adjust field names based on your model
            }
        }
        return JsonResponse(edit)
    except OtherCharge.DoesNotExist:
        return JsonResponse({'error': 'OtherCharge not found'}, status=404)


def updateAddOtherCharge(request):
    if request.method =="POST":
        othercharge_name=request.POST.get("OtherChargeName")
        othercharge_id=request.POST.get("updateAddOtherCharge_id")  
        
        fetchRecord=OtherCharge.objects.get(othercharge_id=othercharge_id)

        fetchRecord.othercharge_name=othercharge_name

        fetchRecord.save()  
        return redirect('/AddOtherCharge/') 






















































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
    
def updaterewardpoint(request):
    if request.method =="POST":
        RewardPoints_id=request.POST.get("RewardPoints_id")
        RewardPoints_Minrange=request.POST.get("RewardPoints_Minrange")
        RewardPoints_Maxrange=request.POST.get("RewardPoints_Maxrange") 
        RewardPoints_Points=request.POST.get("RewardPoints_Points")

        
        fetchRecord=RewardPoints.objects.get(RewardPoints_id=RewardPoints_id)
        if RewardPoints_id:
            fetchRecord.RewardPoints_id=RewardPoints_id
        if RewardPoints_Minrange:
            fetchRecord.RewardPoints_Minrange=RewardPoints_Minrange
        if RewardPoints_Maxrange:
            fetchRecord.RewardPoints_Maxrange=RewardPoints_Maxrange
        if RewardPoints_Points:
            fetchRecord.RewardPoints_Points=RewardPoints_Points


            

        fetchRecord.save()  
        return redirect('/RewardPoints/')     
   
    

def deleteRewardPoints(request,id):
    RewardPointsdata =RewardPoints.objects.get(RewardPoints_id=id)
    RewardPointsdata.delete()
    return redirect('/RewardPoints/')
    





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




def Stock(request):
    return render(request,'stock.html')

def updatepaymentmode(request):
    if request.method=='POST':
        Paymentmode_id = request.POST.get('updatepaymentmode_id')
        Paymentmode_name=request.POST.get('updatepaymentmode_name')

        fetchrecord = Paymentmode.objects.get(Paymentmode_id=Paymentmode_id)
        fetchrecord.Paymentmode_name=Paymentmode_name

        fetchrecord.save()
        return redirect('/paymentmode/')
    else:
        return render(request,'paymentmode.html')
    
def editpaymentmode(request, id):
    try:
        paymentmodedata = Paymentmode.objects.get(Paymentmode_id=id)
        edit = {
            'editpaymentmode': {  # 👈 Make sure this matches what JS expects
                'Paymentmode_id': paymentmodedata.Paymentmode_id,
                'Paymentmode_name': paymentmodedata.Paymentmode_name,
            }
        }
        return JsonResponse(edit)
    except Paymentmode.DoesNotExist:
        return JsonResponse({'error': 'Payment mode not found'}, status=404)
       
    

def insertpaymentmode(request):
    if request.method=='POST':
        Paymentmode_name=request.POST.get('ipaymentmode_name')

        insertpaymentterms=Paymentmode(
            Paymentmode_name=Paymentmode_name
        )

        insertpaymentterms.save()
        return redirect('/paymentmode/')
    else:
        return render(request,'Paymentmode.html')
    
def deletepaymentmode(request,id):
    Paymentmodedata=Paymentmode.objects.get(Paymentmode_id=id)

    Paymentmodedata.delete()

    return redirect('/paymentmode/')
    
def updateproduct(request):
    if request.method == "POST":
       
        id=request.POST.get('product_id'),    
        product_name=request.POST.get('Productname'),
        product_marathi_name=request.POST.get('Marathiname'),
        product_HSNCode=request.POST.get('HSNCode'),
        category=request.POST.get('category'),
        brand=request.POST.get('brand'),
        taxpercent=request.POST.get('tax_percentage'),
        tax=request.POST.get('tax'),
        unit=request.POST.get('unit'),
        alternateunit=request.POST.get('AlternateUnit'),
        conversionfact=request.POST.get('conversion'),
        nos=request.POST.get('unitperprice'),
        barcode=request.POST.get('barcode'),
        #qrcode=request.POST.get('mrp'),
        mrp=request.POST.get('mrp'),
        sale=request.POST.get('sale'),
        credit=request.POST.get('credit'),
        purchase=request.POST.get('Purchase'),
        wholesaler=request.POST.get('Wholesaler'),
        distributor=request.POST.get('Distributor'),
        op_Qty=request.POST.get('Op_Qty'),
        op_Value=request.POST.get('Op_Value'),
        mfg_Date=request.POST.get('MfgDate'),
        exp_Date=request.POST.get('ExpDate')

        fetchRecord=Product.objects.get(product_id=id)
        fetchRecord.product_name=product_name,
        fetchRecord.product_marathi_name=product_marathi_name,
        fetchRecord.product_HSNCode=product_HSNCode,
        fetchRecord.category=category,
        fetchRecord.brand=brand,
        fetchRecord.tax=tax,
        fetchRecord.taxpercent=taxpercent,
        fetchRecord.unit=unit,
        fetchRecord.alternateunit=alternateunit,
        fetchRecord.conversionfact=conversionfact,
        fetchRecord.nos=nos,
        fetchRecord.barcode=barcode,
        fetchRecord.qrcode=brand,
        fetchRecord.mrp=mrp,
        fetchRecord.sale=sale,
        fetchRecord.credit=credit,
        fetchRecord.purchase=purchase,
        fetchRecord.wholesaler=wholesaler,
        fetchRecord.distributor=distributor,
        fetchRecord.op_Qty=op_Qty,
        fetchRecord.op_Value=op_Value,
        fetchRecord.mfg_Date=mfg_Date,
        fetchRecord.exp_Date=exp_Date

        fetchRecord.save()
        return redirect('/products/')

    else:
        return render(request,'productlist.html')    


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
    
def deletepaymentterms(request,id):
    Paymenttermsdata=Paymentterms.objects.get(Paymentterms_id=id)

    Paymenttermsdata.delete()

    return redirect('/Paymentterms/') 

def updatepaymentterms(request):
    if request.method == 'POST':
        Paymentterms_id = request.POST.get('update_paymentterms_id')  # ✅ underscore
        Paymentterms_name = request.POST.get('update_paymentterms_name')

        try:
            fetchrecord = Paymentterms.objects.get(Paymentterms_id=Paymentterms_id)
            fetchrecord.Paymentterms_name = Paymentterms_name
            fetchrecord.save()
        except Paymentterms.DoesNotExist:
            return JsonResponse({'error': 'Paymentterms not found'}, status=404)

        return redirect('/Paymentterms/')
    else:
        return render(request, 'paymentterms.html')

    
def editpaymentterms(request, id):
    try:
        paymenttermsdata = Paymentterms.objects.get(Paymentterms_id=id)
        edit = {
            'editpaymentterms': {  # 👈 Make sure this matches what JS expects
                'Paymentterms_id': paymenttermsdata.Paymentterms_id,
                'Paymentterms_name': paymenttermsdata.Paymentterms_name,
            }
        }
        return JsonResponse(edit)
    except Paymentterms.DoesNotExist:
        return JsonResponse({'error': 'Paymentterms not found'}, status=404)
    
from django.shortcuts import redirect
from django.contrib import messages


def updateuser(request):
    if request.method == "POST":
        users_id = request.POST.get("updateuser_id")

        if not users_id:
            messages.error(request, "User ID missing from request.")
            return redirect('/Users/')

        try:
            fetchRecord = Users.objects.get(users_id=users_id)
            fetchRecord.users_name = request.POST.get("update_user_name")
            fetchRecord.users_email = request.POST.get("update_user_email")
            fetchRecord.users_mobile = request.POST.get("update_mob")
            fetchRecord.users_role = request.POST.get("update_role")
            fetchRecord.users_pass = request.POST.get("update_Pass")
            
            # Save the updated record
            fetchRecord.save()
            messages.success(request, "User updated successfully.")
        except Users.DoesNotExist:
            messages.error(request, "User not found.")

        return redirect('/Users/')
    
    return redirect('/Users/')


       
def edituser(request, id):
    try:
        usersdata = Users.objects.get(users_id=id)
        edit = {
            'edituser': {
                'users_name': usersdata.users_name,
                'users_id': usersdata.users_id,
                'users_email': usersdata.users_email,
                'users_mobile': usersdata.users_mobile,
                'users_role': usersdata.users_role,
                'users_pass': usersdata.users_pass
            }
        }
        return JsonResponse(edit)
    except Users.DoesNotExist:
        return JsonResponse({'error': 'User not found'}, status=404)





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
from datetime import datetime
from django.http import HttpResponse


def parse_date(date_str):
    try:
        if date_str:
            # Match HTML date input format
            return datetime.strptime(date_str, "%Y-%m-%d").date()
    except (ValueError, TypeError):
        pass
    return None


def insertemployee(request):
    
    if request.method == "POST":
        # Get data from POST request
        
        Employees_firstname = request.POST.get("first_name")
        Employees_middlename = request.POST.get("middle_name") 
        Employees_lastname = request.POST.get("last_name")
        Employees_dateof_birth = request.POST.get("date_birth")
        Employees_gender = request.POST.get("gender") or "Not Specified"

        Employees_address = request.POST.get("address")
        Employees_mobile_number = request.POST.get("mob")
        Employees_email = request.POST.get("email_Add")

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
        Employees_iddocument = request.POST.get("id")
        Employees_certificationsdocument = request.POST.get("d_certification")

        department_name = request.POST.get("d_name")
        department_birth = request.POST.get("d_birth")
        d_relationship = request.POST.get("d_relationship")

        if Employees.objects.filter(Employees_email=Employees_email).exists():
            return HttpResponse("Email already exists!")


        # Convert date fields safely using the format yyyy/dd/mm
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

        try:
            Employees_vacationleave_balance = int(request.POST.get("v_leave_balance") or 0)
        except ValueError:
            Employees_vacationleave_balance = 0

        try:
            Employees_sickleave_balance = int(request.POST.get("s_leave_balance") or 0)
        except ValueError:
            Employees_sickleave_balance = 0

        try:
            Employees_salary = float(request.POST.get("salary") or 0)
        except (ValueError, TypeError):
            Employees_salary = 0




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
            employee_id=employee_id,

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
    
def deleteemployee(request,id):
    employeedata =Employees.objects.get(Employees_id=id)
    employeedata.delete()
    return redirect('/Salelist/')

from django.shortcuts import render, redirect
from django.contrib import messages
from datetime import datetime


def updateemployee(request):
    if request.method == "POST":
        Employees_id = request.POST.get("Employee_id")

        try:
            fetchRecord = Employees.objects.get(Employees_id=Employees_id)

            # Handle date conversions
            try:
                fetchRecord.Employees_dateof_birth = datetime.strptime(request.POST.get("Date_birth"), "%Y-%d-%m").date()
            except:
                fetchRecord.Employees_dateof_birth = None

            try:
                fetchRecord.hire_date = datetime.strptime(request.POST.get("Hire_date"), "%Y-%d-%m").date()
            except:
                fetchRecord.hire_date = None

            try:
                fetchRecord.termination_date = datetime.strptime(request.POST.get("Termination_date"), "%Y-%d-%m").date()
            except:
                fetchRecord.termination_date = None

            try:
                fetchRecord.department_birth = datetime.strptime(request.POST.get("D_birth"), "%Y-%d-%m").date()
            except:
                fetchRecord.department_birth = None

            # Update fields
            fetchRecord.Employees_firstname = request.POST.get("ufirst_name")
            fetchRecord.Employees_middlename = request.POST.get("Middle_name")
            fetchRecord.Employees_lastname = request.POST.get("Last_name")
            fetchRecord.Employees_gender = request.POST.get("Gender")

            fetchRecord.Employees_address = request.POST.get("Address")
            fetchRecord.Employees_mobile_number = request.POST.get("Mob")
            fetchRecord.Employees_email = request.POST.get("email_add")

            fetchRecord.Employees_highesteducation = request.POST.get("High_education")
            fetchRecord.Employees_institutionsattended = request.POST.get("Institution_attended")
            fetchRecord.Employees_degreesearned = request.POST.get("Degrees_earned")
            fetchRecord.Employees_certifications = request.POST.get("Certifications")

            fetchRecord.Employees_vacationleave_balance = int(request.POST.get("V_leave_balance") or 0)
            fetchRecord.Employees_sickleave_balance = int(request.POST.get("S_leave_balance") or 0)
            fetchRecord.Employees_leavetypes = request.POST.get("types_leave")

            fetchRecord.Employees_salary = float(request.POST.get("Salary") or 0)
            fetchRecord.Employees_payfrequency = request.POST.get("Pay_frequency")
            fetchRecord.Employees_accountnumber = request.POST.get("Acc_no")
            fetchRecord.Employees_ifsccode = request.POST.get("IFSC_code")
            fetchRecord.Employees_accountholder_name = request.POST.get("Acc_holder")

            fetchRecord.employee_id = request.POST.get("Emp_id")
            fetchRecord.job_title = request.POST.get("Job_title")
            fetchRecord.department = request.POST.get("Dept")
            fetchRecord.employment_status = request.POST.get("Emp_status")

            fetchRecord.Employees_emergencycontact_name = request.POST.get("E_name")
            fetchRecord.Employees_emergencycontact_relationship = request.POST.get("Relationship")
            fetchRecord.Employees_emergencycontact_phone = request.POST.get("Phone_no")

            fetchRecord.department_name = request.POST.get("D_name")
            fetchRecord.d_relationship = request.POST.get("D_relationship")

            fetchRecord.Employees_previous_employers = request.POST.get("P_emp")
            fetchRecord.Employees_previous_jobtitles = request.POST.get("Job_titles")
            fetchRecord.Employees_previous_responsibilities = request.POST.get("Responsibilities")

            # Handle file uploads (case-sensitive field names)
            if 'resume' in request.FILES:
                fetchRecord.Employees_resume = request.FILES['resume']
            if 'id' in request.FILES:
                fetchRecord.Employees_iddocument = request.FILES['id']
            if 'd_certification' in request.FILES:
                fetchRecord.Employees_certificationsdocument = request.FILES['d_certification']

            fetchRecord.save()
            messages.success(request, "Employee updated successfully.")
            return redirect('/Employee/')

        except Employees.DoesNotExist:
            messages.error(request, "Employee not found.")
            return redirect('/Employees/')


def Addsale(request):
    if request.method == 'POST':
        Sales_name = request.POST.get('Sales_name')  # dropdown with "Cash Sale" / "Credit Sale"
        invoice_no = request.POST.get('Sales_invoice_no')

        payment_term = request.POST.get('sales_mode')  # Cash or Credit
        invoice_date = request.POST.get('add_invoicedate')
        due_days = request.POST.get('add_duedays') or 0
        due_date = request.POST.get('add_duedate') or invoice_date
        product_name = request.POST.get('add_productname')
        qty = int(request.POST.get('Sales_qty') or 0)
        sale_price = float(request.POST.get('Sales_price') or 0)

        mrp = float(request.POST.get('Sales_mrp') or 0)
        dis_percent = float(request.POST.get('Sales_discount_percent') or 0)
        gst_percent = float(request.POST.get('Sales_gst_percent') or 0)

        # Calculations
        discount_value = (mrp * qty) * (dis_percent / 100)
        basic_total = (mrp * qty) - discount_value
        gst_value = basic_total * (gst_percent / 100)
        grand_total = basic_total + gst_value
        grand_total = request.POST.get('Sales_grand_total') or 0


        sale = Sales.objects.create(
            Sales_name=Sales_name,
            Sales_invoice_no=invoice_no,
            Sales_payment_term=payment_term,
            Sales_addinvoicedate=invoice_date,
            Sales_add_duedays=due_days,
            Sales_add_duedate=due_date,
            Sales_addproductname=product_name,
            Sales_qty=qty,
             Sales_price=sale_price, 
             Sales_mrp=mrp,
            Sales_discount_percent=dis_percent,
            Sales_discount_value=discount_value,
            Sales_basic_total=basic_total,
            Sales_gst_percent=gst_percent,
            Sales_gst_value=gst_value,
            Sales_grand_total=grand_total
        )
        sale.save()
        

        messages.success(request, "Sale added successfully!")
        return redirect('/Salelist/')
    saledata = Sales.objects.all().order_by('-Sales_id')
    return render(request, 'addsale.html', {'saledata': saledata})

def deletesale(request,id):
    saledata =Sales.objects.get(Sales_id=id)
    saledata.delete()
    return redirect('/Salelist/')

# 👉 Sale List View
def salelist(request):
    sales = Sales.objects.all().order_by('-Sales_id')
    return render(request, 'sales/sale_list.html', {'sales': sales})

def updatesale(request):
    
    if request.method == "POST":
        Sales_id = request.POST.get("updatesale_id")

        if not Sales_id:
            messages.error(request, "Sale ID  missing from request.")
            return redirect('/Salelist/')

        try:
            fetchRecord = Sales.objects.get(Sales_id=Sales_id)
            fetchRecord.Sales_name = request.POST.get("Sales_name")
            fetchRecord.Sales_payment_term = request.POST.get("sales_mode")
            fetchRecord.Sales_addinvoicedate = request.POST.get("add_invoicedate")
            fetchRecord.Sales_add_duedays = request.POST.get("add_duedays")
            fetchRecord.Sales_add_duedate = request.POST.get("add_duedate")
            fetchRecord.Sales_addproductname = request.POST.get("add_productname")
            
            # Save the updated record
            fetchRecord.save()
            messages.success(request, "Sale updated successfully.")
        except Sales.DoesNotExist:
            messages.error(request, "Sale not found.")

        return redirect('/Salelist/')
    
 
from django.http import JsonResponse



def editsale(request, id):
    try:
        saledata = Sales.objects.get(Sales_id=id)
        edit = {
            'editsale': {
                'Sales_name': saledata.Sales_name,
                'Sales_id': saledata.Sales_id,
                'Sales_payment_term': saledata.Sales_payment_term,
                'Sales_addinvoicedate': saledata.Sales_addinvoicedate.strftime('%Y-%m-%d') if saledata.Sales_addinvoicedate else '',
                'Sales_add_duedays': saledata.Sales_add_duedays,
                'Sales_add_duedate': saledata.Sales_add_duedate.strftime('%Y-%m-%d') if saledata.Sales_add_duedate else '',
                'Sales_addproductname': saledata.Sales_addproductname,
                'Sales_qty': saledata.Sales_qty,
                'Sales_mrp': float(saledata.Sales_mrp or 0),
                'Sales_discount_percent': float(saledata.Sales_discount_percent or 0),
                'Sales_discount_value': float(saledata.Sales_discount_value or 0),
                'Sales_basic_total': float(saledata.Sales_basic_total or 0),
                'Sales_gst_percent': float(saledata.Sales_gst_percent or 0),
                'Sales_gst_value': float(saledata.Sales_gst_value or 0),
                'Sales_grand_total': float(saledata.Sales_grand_total or 0),
            }
        }
        return JsonResponse(edit)

    except Sales.DoesNotExist:
        return JsonResponse({'error': 'Sale not found'}, status=404)

def posview(request):
    query = request.GET.get('search', '')  # Get search input from request
    customer=Customer.objects.all()
    products = Product.objects.filter(name__icontains=query) if query else Product.objects.all()
    return render(request,'Pos1.html',{'products': products, 'search_query': query,'customer':customer})


def get_product_names(request):
    products = list(Product.objects.values_list('name', flat=True))  # Get only product names
    return JsonResponse({'products': products})

def get_customer_details(request,id):

    
    customer = get_object_or_404(Customer, customer_id=id)

    data = {
        "mobile_no": customer.customer_mobile,
        "address": customer.customer_ShippingAddress,
        "credit_amt": customer.customer_CreditLimit,
    #      "mobile_no": "9876543210",
    #     "address": "123 Street",
    #    "credit_amt": "100.00"
    }
    return JsonResponse(data)

from poschild.models import Poschild

def insertpos(request):
    if request.method=="POST":

        productname=request.POST.getlist('productname[]')
        productid=request.POST.getlist('productid[]')
       
        productqty=request.POST.getlist('productqty[]')
     
        productmrp=request.POST.getlist('mrp[]')
        
        productsale=request.POST.getlist('sale[]')
       
        totalprice=request.POST.getlist('totalprice[]')  
        
        customer_id=int(request.POST.get('customername'))
        paymentmode=request.POST.get('paymentmode')
        billdate=request.POST.get('billdate')
        total_amount=request.POST.get('total_amount')
    
        insertdata=Master(
            customer_id=Customer.objects.get(customer_id = customer_id),             
            master_payment_mode=paymentmode,
            master_billdate=billdate,
            master_totalAmount=total_amount
        )
        insertdata.save() 


        print(len(productid))
        productid = list(productid)
        try:
            for i in range(len(productid)):
                chliddata=Poschild(
                    master_id= insertdata,
                    customer_id=Customer.objects.get(customer_id = customer_id), 
                    product_id=Product.objects.get(product_id = int(productid[i])), 
                    item_name=productname[i],
                    item_qty=productqty[i],
                    item_mrp=productmrp[i],
                    item_saleprice=productsale[i],
                    item_total=totalprice[i]    
                )
                chliddata.save()
                id=insertdata.master_id

            return redirect('POSBillshow', id=insertdata.master_id)     

        except Exception as e:
            print("Error saving Poschild:", e) 
            return render(request,'pos1.html') 
    
    else:
        return redirect('POSBillshow', id=id)   
         


def POSBillshow(request, id):
    # Get the master bill record
    master = get_object_or_404(Master, master_id=id)
    
    # Get all child items for this bill
    
    
    context = {
        'master': master
         
    }
    
    return render(request, 'POSBills.html', context)

# def posview(request):
#     from_date = request.GET.get('from_date')
#     to_date = request.GET.get('to_date')
    
#     master = Master.objects.all().order_by('-master_billdate')
    
#     if from_date and to_date: 
#         master = master.filter(
#             master_billdate__gte=from_date,
#             master_billdate__lte=to_date
#         )
    
#     context = {
#         'master': master,
#     }
#     return render(request, 'POSBills.html', context)

def Dashboard(request):
    return render(request,'Dashboard.html')