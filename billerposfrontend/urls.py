"""
URL configuration for billerposfrontend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from billerposfrontend import settings
from django.conf.urls.static import static
from billerposfrontend import views
from tax.views import taxlist,inserttax,deletetax,edittax
from product.views import insertproduct


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('index/', views.index),
    path('login/', views.login),
    path('register/', views.register),
    path('category/',views.category),
    path('insertcategory/',views.insertcategory),
    path('editcategory/<id>/',views.editcategory),
    path('updatecategory/',views.updatecategory),
    path('category/deleteCategory/<id>',views.deleteCategory),

    path('deleteCategory/<id>/',views.deleteCategory),

<<<<<<< HEAD
   
=======
>>>>>>> b90315084a90106d203c7198eed8b1811e0113d5

    path('brand/',views.brand),
    path('insertbrand/',views.insertbrandpage),
    path('editbrand/<id>/',views.editbrand),
    path('updatebrand/',views.updatebrand),
    path('brand/deleteBrand/<id>',views.deleteBrand),
    path('tax/',taxlist),
    path('inserttax/',inserttax),
    path('edittax/<id>/',edittax),
    path('tax/deletetax/<id>',deletetax),
    path('products/',views.productslist), 
   
    path('products/',views.productslist),
    path('insertproduct/',insertproduct),
    path('editproduct/<id>/',views.editproduct),
    path('deleteproduct/<id>/',views.deleteproduct),
   
    path('unit/',views.unitlist),  
    path('Addunit/',views.AddUnit),
    path('updateunit/',views.updateunit),
    path('AddUnit/deleteunit/<id>',views.deleteunit),

    path('updateExpenses/',views.updateExpenses),
    # path('saveExpenses/',views.expenseslist), 
    path('AddExpenses/',views.expenseslist),
    path('insertexpenses/',views.insertexpenses),
    path('AddExpenses/deleteexpenses/<id>',views.deleteexpenses),



    path('AddOtherCharge/',views.chargelist),  
    path('AddOtherCharge/',views.OtherCharge),
   ## path('updateAddOtherCharge/',views.updateAddOtherCharge),
    path('insertcharge/',views.insertcharge),
    path('AddOtherCharge/deleteothercharge/<id>',views.deleteothercharge),




    path('Customergrouplist/',views.Customergrouplist),
    path('insertcustomergroup/',views.insertcustomergroup),
    path('editcustomergroup/<id>/',views.editcustomergroup),
    path('updatecustomergroup/',views.updatecustomergroup),
    path('Customergrouplist/deleteCustomergroup/<id>/',views.deleteCustomergroup),
    path('Suppliergrouplist/',views.Suppliergrouplist),
    path('insertsuppliergroup/',views.insertsuppliergroup),
    path('editsuppliergroup/<id>/',views.editsuppliergroup),
    path('updatesuppliergroup/',views.updatesuppliergroup),
    path('Suppliergrouplist/deleteSuppliergroup/<id>/',views.deleteSuppliergroup),

    path('updatecustomer/',views.updatecustomer),
    path('Customerpage/deleteCustomer/<id>',views.deleteCustomer),
    path('insertsuppliergroup/',views.insertsuppliergroup),
    path('paymentmode/',views.paymentmodelist),
    path('Paymentterms/',views.Paymenttermslist),
    path('insertpaymentmode/',views.insertpaymentmode),
    path('insertpaymentterms/',views.insertpaymentterms),
    path('Users/deleteusers/<id>',views.deleteusers),
    path('Supplierlist/',views.Supplierpage),
<<<<<<< HEAD

    path('RewardPoints/',views.RewardPointslist),
=======
    path('RewardPoints/',views.RewardPoints),
>>>>>>> b90315084a90106d203c7198eed8b1811e0113d5
    path('Customerpage/',views.Customerpage),
    path('insertcustomer/',views.insertcustomer),
    path('editcustomer/<id>/',views.editcustomer),
    path('Supplierpage/',views.Supplierpage),
    path('insertsupplier/',views.insertsupplier),
    path('editsupplier/<id>/',views.editsupplier),
    path('updatesupplier/',views.updatesupplier),
    path('Supplierpage/deleteSupplier/<id>',views.deleteSupplier),


    

    path('Employee/',views.Employee),
    path('Users/',views.Userslist),
    path('POSBill/',views.POSBill),
    path('printpage/',views.printpage),
    path('Roles/',views.Roleslist),
    path('EditRole/',views.EditRolelist),
    path('insertroles/',views.insertroles),
    path('Dashboard/',views.Dashboard),
    path('paymentmode/deletepaymentmode/<id>',views.deletepaymentmode),
    path('Barcode/',views.Barcodepage),
    path('stock/',views.stock),
    path('Salelist/',views.Salelist),
    path('Barcode/',views.Barcodepage),
    path('Addsale/',views.Addsale),
    path('Paymentterms/deletepaymentterms/<id>',views.deletepaymentterms),
    path('updatepaymentmode/',views.updatepaymentmode),
    path('updatepaymentterms/<int:id>/', views.updatepaymentterms),
    path('adduser/',views.adduser),
    path('updateuser/',views.updateuser)
   
    

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
