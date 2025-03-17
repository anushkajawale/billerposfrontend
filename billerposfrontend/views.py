from django.shortcuts import render,redirect,HttpResponse
from category.models import Category

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

def editcategory(request,id):
    categorydata=Category.objects.get(category_id=id)
      


    edit={
        'editcategory':categorydata
    }
    return render(request,'category.html',edit)




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
        category_id=request.POST.get("categoryId")
        category_name=request.POST.get("categoryName")
        category_img=request.FILES.get("categoryimg")
        category_bannerimg=request.FILES.get("categoryBanner") 

        fetchRecord=Category.objects.get(category_id=category_id)

        fetchRecord.category_name=category_name
        fetchRecord.category_img=category_img
        fetchRecord.category_bannerimg=category_bannerimg

        fetchRecord.save()  
        return redirect('/category/')
     


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




