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

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index),
    path('login/', views.login),
    path('register/', views.register),
    path('category/',views.category),
    path('insertcategory/',views.insertcategory),
    path('editcategory/<id>/',views.editcategory),
    path('updatecategory/',views.updatecategory),
    path('brand/',views.brand),
    path('tax/',views.tax),
    path('products/',views.productslist),
    
    path('AddUnit/',views.AddUnit),
    path('AddExpenses/',views.AddExpenses),
    path('AddOtherCharge/',views.AddOtherCharge),
    path('Customerlist/',views.Customergrouplist),

    path('insertcustomergroup/',views.insertcustomergroup),
    path('insertsuppliergroup/',views.insertsuppliergroup),

   

    path('Supplierlist/',views.Suppliergrouplist),
    path('paymentmode/',views.paymentmodelist),
    path('Paymentterms/',views.Paymenttermslist),
    
   
    path('RewardPoints/',views.RewardPoints),
    path('Customerpage/',views.Customerpage),
    path('Supplier/',views.Supplierpage),
    path('Employee/',views.Employee),
    path('Roles/',views.Roleslist),
   
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
