from django.shortcuts import render, redirect
from .models import Supplier, Product

def landingview(request):
    return render(request, 'landingpage.html')

# Product view´s
def productlistview(request):
    return render(request, 'productlist.html')

# Supplier view´s
def supplierlistview(request):
    supplierlist = Supplier.objects.all()
    context = {'suppliers': supplierlist}
    return render (request,"supplierlist.html",context)

def addsupplier(request):
    a = request.POST['companyname']
    b = request.POST['contactname']
    c = request.POST['address']
    d = request.POST['phone']
    e = request.POST['email']
    f = request.POST['country']
    Supplier(companyname = a, contactname = b, address = c, phone = d, email = e, country = f).save()
    return redirect(request.META['HTTP_REFERER'])
    