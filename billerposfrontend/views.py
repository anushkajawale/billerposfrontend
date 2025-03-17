from django.shortcuts import render

def index (request):
    return render(request,"index.html")

def login (request):
    return render(request,"login.html")

def register (request):
    return render(request,"register.html")

def category(request):
    return render(request,'category.html')

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
    return render(request, 'Customergroup.html')

def supplierlist(request):
    supplierData = Supplier.objects.all()
    data ={
        "supplier":supplierData
    }  
    return render(request,"Supplierlist.html",data) 

def Paymentmode(request):
    return render(request,'Paymentmode.html')

def Paymentterms(request):
    return render(request,'Paymentterms.html')

def RewardPoints(request):
    return render(request,'RewardPoints.html')

def Customer(request):
    return render(request,'Customers.html')

def Supplier(request):
    return render(request,'Suppliers.html')




