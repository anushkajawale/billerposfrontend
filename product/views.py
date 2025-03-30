from django.shortcuts import render,redirect
from django.http import JsonResponse
from .models import Product
from category.models import Category
from brand.models import Brand
from tax.models import Tax
from Unit.models import Unit


def insertproduct(request):
    if request.method=="POST":
        Productname=request.POST.get('Productname')
        Marathiname=request.POST.get('Marathiname')
        HSNCode=request.POST.get('HSNCode')
        category=request.POST.get('category')
        brand=request.POST.get('brand')
        tax_percentage=request.POST.get('tax_percentage')
        tax=request.POST.get('tax')
        unit=request.POST.get('unit')
        AlternateUnit=request.POST.get('AlternateUnit')
        conversion=request.POST.get('conversion')
        unitperprice=request.POST.get('unitperprice')
        barcode=request.POST.get('barcode')
        qrcode=request.POST.get('qrcode')
        mrp=request.POST.get('mrp')
        sale=request.POST.get('sale')
        credit=request.POST.get('credit')
        Purchase=request.POST.get('Purchase')
        Wholesaler=request.POST.get('Wholesaler')
        Distributor=request.POST.get('Distributor')
        Op_Qty=request.POST.get('Op_Qty')
        Op_Value=request.POST.get('Op_Value')
        MfgDate=request.POST.get('MfgDate')
        ExpDate=request.POST.get('ExpDate')

        insertproduct=Product(
            product_name=Productname,
            product_marathi_name=Marathiname,
            product_HSNCode=HSNCode,   
            category=Category.objects.get(category_id = category),
            brand=Brand.objects.get(brand_id = brand),
            taxpercent=tax_percentage,
            tax=Tax.objects.get(tax_id = tax),
            unit=Unit.objects.get(unit_id = unit),
            alternateunit=AlternateUnit,
            conversionfact=conversion,
            nos=unitperprice,
            barcode=barcode,
            qrcode=qrcode,
            mrp=mrp,
            sale=sale,
            credit=credit,
            purchase=Purchase,
            wholesaler=Wholesaler,
            distributor=Distributor,
            op_Qty=Op_Qty,
            op_Value=Op_Value,
            mfg_Date=MfgDate,
            exp_Date=ExpDate
                              
        )

        insertproduct.save()
        return redirect("/products/")
    else:
        return render(request,'productlist.html') 




  



           
# Create your views here.
