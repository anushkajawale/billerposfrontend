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
    path('deleteCategory/<id>/',views.deletecategory),
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
    path('insertproduct/',insertproduct),
    path('editproduct/<id>/',views.editproduct),
    path('deleteproduct/<id>/',views.deleteproduct),
    path('AddUnit/',views.AddUnit),
    path('updateunit/',views.updateunit),
    path('AddUnit/deleteunit/<id>',views.deleteunit),
    path('AddExpenses/',views.AddExpenses),
    path('AddExpenses/deleteexpenses/<id>',views.deleteexpenses),
    path('AddOtherCharge/',views.AddOtherCharge),
    path('AddOtherCharge/deleteothercharge/<id>',views.deleteothercharge),
    path('Customergrouplist/',views.Customergrouplist),
    path('insertcustomergroup/',views.insertcustomergroup),
    path('editcustomergroup/<id>/',views.editcustomergroup),
    path('updatecustomergroup/',views.updatecustomergroup),
    path('Suppliergrouplist/',views.Suppliergrouplist),
    path('insertsuppliergroup/',views.insertsuppliergroup),
    path('editsuppliergroup/<id>/',views.editsuppliergroup),
    path('updatesuppliergroup/',views.updatesuppliergroup),
    path('updatecustomer/',views.updatecustomer),
    path('insertsuppliergroup/',views.insertsuppliergroup),
    path('paymentmode/',views.paymentmodelist),
    path('Paymentterms/',views.Paymenttermslist),
    path('Supplierlist/',views.Supplierpage),
    path('RewardPoints/',views.RewardPoints),
    path('Customerpage/',views.Customerpage),
    path('editcustomer/<id>/',views.editcustomer),
    path('Supplierpage/',views.Supplierpage),
    path('Employee/',views.Employee),
    path('Users/',views.Userslist),
    path('POSBill/',views.POSBill),
    path('printpage/',views.printpage),
    path('Roles/',views.Roleslist),
    path('Salelist/',views.Salelist),
    path('Barcode/',views.Barcodepage)

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
