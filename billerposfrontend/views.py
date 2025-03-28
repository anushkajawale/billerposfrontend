from django.shortcuts import render,redirect,HttpResponse
from django.shortcuts import render
from django.http import JsonResponse
from Paymentmode.models import Paymentmode
from Paymentterms.models import Paymentterms
from category.models import Category
from supplier.models import Supplier
from customer.models import Customer
from Roles.models import Roles
from django.contrib import messages
from django.db.models import Sum





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
    customerData = Customer.objects.all()
    data ={
        "customer":customerData
    }  
    
    return render(request, 'Customergroup.html',data)


def Supplierlist(request):
    return render(request,'Supplierlist.html')
 
def Paymenttermslist(request):
    listdata = Paymentterms.objects.all()
    data = {
        "list":listdata
    }
    return render(request,'Paymentterms.html',data)

def supplierlist(request):
    supplierData = Supplier.objects.all()
    data ={
        "supplier":supplierData
    }  
    return render(request,"Supplierlist.html",data) 

def productslist(request):
    return render(request,'productlist.html')
    


def Employee(request):
    return render(request,'Employee.html')

def RewardPoints(request):
    return render(request,'RewardPoints.html')

def Customer(request):
    return render(request,'Customers.html')

def Supplier(request):
    return render(request,'Suppliers.html')


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