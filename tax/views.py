from django.shortcuts import render,redirect
from .models import Tax
from django.http import JsonResponse




def taxlist(request):
    taxdata=Tax.objects.all()
    data={
        'taxdata':taxdata
    }
    
    return render(request,'tax.html',data)

def inserttax(request):
    if request.method=="POST":
        taxname=request.POST.get('TaxName')
        percentage=request.POST.get('percentage')

        taxdata=Tax(
            tax_name=taxname,
            tax_percentage=percentage

        )

        taxdata.save()
        return redirect('/tax/')

def edittax(request,id):
    try:
        taxdata=Tax.objects.get(tax_id=id)  
        edit = {
            'edittax': {
                'tax_id': taxdata.tax_id,
                'tax_name': taxdata.tax_name, 
                'tax_percentage':taxdata.tax_percentage   # Adjust field names based on your model
            }
        }
        return JsonResponse(edit)
    except Tax.DoesNotExist:
        return JsonResponse({'error': 'Tax not found'}, status=404)

      

    


def deletetax (request,id):
    taxdata=Tax.objects.get(tax_id=id)
    taxdata.delete()
    return redirect('/tax/')



# Create your views here.
