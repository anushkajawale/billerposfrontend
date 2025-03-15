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
    return render(request, 'Customerlist.html')

def Supplierlist(request):
    return render(request,'Supplierlist.html')

def Paymentmode(request):
    return render(request,'Paymentmode.html')

def Paymentterms(request):
    return render(request,'Paymentterms.html')


def Employee(request):
    return render(request,'Employee.html')

def RewardPoints(request):
    return render(request,'RewardPoints.html')




