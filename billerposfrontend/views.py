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
from customer.models import Customer

from supplier.models import Supplier

from Users.models import Users






def index (request):
    return render(request,"index.html")

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
    
def deletecategory(request):
     return render(request,'category.html')

     

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




def tax(request):
    return render(request,'tax.html')





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
            fetchRecord.ustomergroup_id=customergroup_id
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
    return render(request,'productlist.html')
    


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


