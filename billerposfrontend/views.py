from django.shortcuts import render,redirect
from category.models import Category
from supplier.models import Supplier
from customer.models import Customer
# from customergroup.models import Customergroup

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

def brand(request):
    return render(request,'brand.html')

def tax(request):
    return render(request,'tax.html')


def AddUnit(request):
    return render(request,'AddUnit.html')

def AddExpenses(request):
    return render(request,'AddExpenses.html')

def AddOtherCharge(request):
    return render(request,'AddOtherCharge.html')

def Customerlist(request):
     customerData = Customer.objects.all()
     data ={
         "customer":customerData
     }  
    
     return render(request, 'Customergroup.html',data)

def insertcustomergroup(request):
    if request.method=='POST':
        customergroup=request.POST.get('customergroupname')

        # insertquery=Customergroup(
        # customergroup_name=customergroup
        # )  

        # insertquery.save() 
        return redirect("/Customerlist/")
    else:
        return render(request,'Customergroup.html') 



def supplierlist(request):
    supplierData = Supplier.objects.all()
    data ={
        "supplier":supplierData
    }  
    return render(request,"Supplierlist.html",data) 

def productslist(request):
    return render(request,'productlist.html')
    

def Paymentmode(request):
    return render(request,'Paymentmode.html')

def Paymentterms(request):
    return render(request,'Paymentterms.html')


def Employee(request):
    return render(request,'Employee.html')

def RewardPoints(request):
    return render(request,'RewardPoints.html')

def Customerpage(request):
    return render(request,'Customers.html')

def Supplierpage(request):
    return render(request,'Suppliers.html')








