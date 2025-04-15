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

    path('', views.login),
    path('index/', views.index),

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
    path('brand/',views.brand),
    path('insertbrand/',views.insertbrandpage),
    path('editbrand/<id>/',views.editbrand),
    path('updatebrand/',views.updatebrand),
    path('brand/deleteBrand/<id>',views.deleteBrand),
    path('tax/',taxlist),
    path('inserttax/',inserttax),
    path('edittax/<id>/',edittax),
    path('tax/deletetax/<id>',deletetax),  
    path('unit/',views.unitlist),  
    path('Addunit/',views.AddUnit),
    path('products/',views.productslist), 
    path('products/',views.productslist),
    path('insertproduct/',insertproduct),
    path('editproduct/<id>/',views.editproduct),
    path('updateproduct/',views.updateproduct),
    path('deleteproduct/<id>/',views.deleteproduct),  
    path('unit/',views.unitlist),  
    path('Addunit/',views.AddUnit),
    path('editunit/<id>/',views.editAddUnit),
    path('updateunit/',views.updateunit),
    path('unit/deleteunit/<id>',views.deleteunit),


    #path('updateexpenses/',views.updateexpenses),
    #path('editAddExpenses/<id>/',views.editAddExpenses),
    path('AddExpenses/',views.expenseslist),
    path('insertexpenses/',views.insertexpenses),
    path('AddExpenses/deleteexpenses/<id>',views.deleteexpenses),


   # path('updateExpenses/',views.updateExpenses),
     path('saveExpenses/',views.expenseslist), 
    path('AddExpenses/',views.expenseslist),
    path('insertexpenses/',views.insertexpenses),
    path('AddExpenses/deleteexpenses/<id>',views.deleteexpenses),
    path('AddOtherCharge/',views.chargelist),  
    path('updateAddOtherCharge/',views.updateAddOtherCharge),
    path('insertcharge/',views.insertcharge),
    path('AddOtherCharge/deleteothercharge/<id>',views.deleteothercharge),
    path('editAddOtherCharge/<id>',views.editAddOtherCharge),
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
    path('editpaymentmode/<id>/',views.editpaymentmode),
    path('Paymentterms/',views.Paymenttermslist),
    path('insertpaymentmode/',views.insertpaymentmode),
    path('insertpaymentterms/',views.insertpaymentterms),
    path('Users/deleteusers/<id>',views.deleteusers),
    path('edituser/<id>/',views.edituser),
    path('Supplierlist/',views.Supplierpage),
    path('RewardPoints/',views.RewardPointslist),
    path('RewardPoints/',views.RewardPoints), 

    path('insertrewardpoint/',views.insertrewardpoint),
    path('editrewardpointpage/<id>/',views.editrewardpointpage),
    path('updaterewardpoint/',views.updaterewardpoint),

    path('RewardPoints/deleteRewardPoints/<id>',views.deleteRewardPoints),
    
    path('Customerpage/',views.Customerpage),
    path('insertcustomer/',views.insertcustomer),
    path('editcustomer/<id>/',views.editcustomer),
    
    path('Customerpage/deleteCustomer/<id>',views.deleteCustomer),
    path('Supplierpage/',views.Supplierpage),
    path('insertsupplier/',views.insertsupplier),
    path('editsupplier/<id>/',views.editsupplier),
    path('updatesupplier/',views.updatesupplier),
    path('Supplierpage/deleteSupplier/<id>',views.deleteSupplier),

    path('Employee/',views.Employee),
    path('editEmployee/<id>/',views.editEmployeeModal),
    path('Users/',views.Userslist),
    path('POSBill/',views.POSBill),
    path('printpage/',views.printpage),
    path('Roles/',views.Roleslist),
    path('Roles/deleteRoles/<id>',views.deleteRoles),
  


    path('EditRole/<id>/',views.EditRoles),
    path('insertroles/',views.insertroles),


    path('Dashboard/',views.Dashboard),


    path('logout/',views.logout),
    path('updateemployee/<int:id>',views.updateemployee),

    path('EditRole/',views.updateroles),
    path('insertroles/',views.insertroles),

    path('paymentmode/deletepaymentmode/<id>',views.deletepaymentmode),
    

    path('paymentmode/deletepaymentmode/<id>',views.deletepaymentmode),
    path('paymentmode/deletepaymentmode/<id>',views.deletepaymentmode),



    path('Barcode/',views.Barcodepage),
    path('stock/',views.stock),
    path('Salelist/',views.Salelist),
    path('Barcode/',views.Barcodepage),
    path('Addsale/',views.Addsale),

    path('posview/',views.posview),
    path('get-product-names/', views.get_product_names, name='get_product_names'),
    path('insertpos/',views.insertpos),

    path('BillWiselist/',views.BillWiselist),
    path('OutstandingReport/',views.OutstandingReport),
    path('LedgerReport/',views.LedgerReport),
    path('POSRegisterReport/',views.POSRegisterReport),
    path('PrintLedgerReport/',views.PrintLedgerReport),
    path('PrintOutStandingReport/',views.PrintOutStandingReport),
    path('PrintPOSRegisterReport/',views.PrintPOSRegisterReport),
    path('PrintBillWiseReport/',views.PrintBillWiseReport),

    path('Paymentterms/deletepaymentterms/<id>',views.deletepaymentterms),
    path('updatepaymentmode/',views.updatepaymentmode),
    path('updatepaymentterms/', views.updatepaymentterms),
    path('adduser/',views.adduser),
    path('updateuser/',views.updateuser),
    
    path('insertemployee/',views.insertemployee),
    path('editpaymentterms/<id>/',views.editpaymentterms),
    path('Employee/deleteemployee/<id>',views.deleteemployee),
    path('Salelist/deletesale/<id>',views.deletesale),
    path('updatesale/',views.updatesale),
    path('editsale/<id>/',views.editsale),

 
    path('Paymentterms/deletepaymentterms/<id>',views.deletepaymentterms),
    path('updatepaymentmode/',views.updatepaymentmode),
    path('updatepaymentterms/<int:id>/', views.updatepaymentterms),
    path('adduser/',views.adduser),
    path('updateuser/',views.updateuser),   
    path("get-customer-details/<id>/", views.get_customer_details),
    path('POSBill/<int:id>/', views.POSBillshow, name='POSBillshow'),
    path('receipt/', views.receipt_view, name='receipt'),


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
