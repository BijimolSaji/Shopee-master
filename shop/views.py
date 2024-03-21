from django.http import JsonResponse, HttpResponse
from django.shortcuts import render

from admin.models import tbl_subcategory, tbl_category
from company.models import tbl_comproduct, tbl_unit, tbl_company
from shop.models import tbl_shopproduct, tbl_shop, tbl_cprdrequest


# Create your views here.
def home(request):
    return render(request, "shop/home.html")


def cproductview(request):
    category = tbl_category.objects.all()
    emp = tbl_comproduct.objects.all()
    return render(request, "shop/cproductview.html", {'comproduct': emp, 'category': category})


def fillsubcategory(request):
    did = int(request.POST.get("did"))
    subcategory = tbl_subcategory.objects.filter(categoryid=did).values()
    return JsonResponse(list(subcategory), safe=False)


def fillproduct(request):
    did = int(request.POST.get("did"))
    product = tbl_comproduct.objects.filter(subcategoryid=did).values()
    return JsonResponse(list(product), safe=False)


def cproductdetails(request, id):
    if request.method == 'POST':
        reobj = tbl_cprdrequest()
        c = request.session.get('loginid')
        reobj.shopid = tbl_shop.objects.get(loginid=c)
        reobj.quantity = request.POST.get('quantity')
        reobj.totalprice = request.POST.get('totalamount')
        reobj.comments = request.POST.get('comments')
        reobj.status = 'requested'
        reobj.companyid = tbl_company.objects.get(companyid=request.POST.get('companyid'))
        reobj.comproductid = tbl_comproduct.objects.get(comproductid=request.POST.get('comproductid'))
        reobj.unitid = tbl_unit.objects.get(unitid=request.POST.get('unitid'))
        reobj.save()
        return HttpResponse("<script>alert('Order request send Successfully');window.location='/Shop/comproductview/';</script>")
    else:
        emp = tbl_comproduct.objects.get(comproductid=id)
        return render(request, "shop/cproductdetails.html", {'comproduct': emp})


def productreg(request):
    if request.method == 'POST':
        shopobj = tbl_shopproduct()
        c = request.session.get('loginid')
        shopobj.shopid = tbl_shop.objects.get(loginid=c)
        shopobj.shopproductname = request.POST.get('shopproductname')
        shopobj.shopproductdesc = request.POST.get('shopproductdesc')
        shopobj.price = request.POST.get('price')
        shopobj.stock = request.POST.get('stock')
        shopobj.categoryid = tbl_category.objects.get(categoryid=request.POST.get('category'))
        shopobj.subcategoryid = tbl_subcategory.objects.get(subcategoryid=request.POST.get('subcategory'))
        unit = request.POST.get('unit')
        shopobj.unitid = tbl_unit.objects.get(unitid=unit)
        shopobj.save()
        return HttpResponse(
            "<script>alert('Product Registered Successfully');window.location='/Shop/productreg/';</script>")
    else:
        category = tbl_category.objects.all()
        unit = tbl_unit.objects.all()
        return render(request, 'shop/productreg.html', {'category': category, 'unit': unit})


def fillsubcategory(request):
    did = int(request.POST.get("did"))
    subcategory = tbl_subcategory.objects.filter(categoryid=did).values()
    return JsonResponse(list(subcategory), safe=False)


def productview(request):
    c = request.session.get('loginid')
    shopid = tbl_shop.objects.get(loginid=c)
    emp = tbl_shopproduct.objects.filter(shopid=shopid)
    return render(request, "shop/productview.html", {'shopproduct': emp})


def deleteshopproduct(request, id):
    emp = tbl_shopproduct.objects.get(shopproductid=id)
    emp.delete()
    return HttpResponse(
        "<script>alert('Product Deleted Successfully');window.location='/Shop/shopproductview/';</script>")


def shopproductedit(request, id):
    if request.method == 'POST':
        category = request.POST.get('category')
        subcategoryid = request.POST.get('subcategory')
        unit = request.POST.get('unit')
        shopproductname = request.POST.get('shopproductname')
        shopproductdesc = request.POST.get('shopproductdesc')
        price = request.POST.get('price')
        stock = request.POST.get('stock')
        emp = tbl_shopproduct.objects.get(shopproductid=id)
        emp.shopproductname = shopproductname
        emp.shopproductdesc = shopproductdesc
        emp.price = price
        emp.stock = stock
        emp.categoryid = tbl_category.objects.get(categoryid=category)
        emp.subcategoryid = tbl_subcategory.objects.get(subcategoryid=subcategoryid)

        emp.unitid = tbl_unit.objects.get(unitid=unit)
        emp.save()
        return HttpResponse(
            "<script>alert('Product Edited Successfully');window.location='/Shop/shopproductview/';</script>")
    category = tbl_category.objects.all()
    unit = tbl_unit.objects.all()
    emp = tbl_shopproduct.objects.get(shopproductid=id)
    return render(request, "shop/shopproductedit.html", {'emp': emp, 'category': category, 'unit': unit})


def sales(request):
    c = request.session.get('loginid')
    shopid = tbl_shop.objects.get(loginid=c)
    category = tbl_category.objects.all()
    emp = tbl_shopproduct.objects.filter(shopid=shopid)
    return render(request, "shop/sales.html", {'shopproduct': emp, 'category': category})


def fillshopproduct(request):
    did = int(request.POST.get("did"))
    product = tbl_shopproduct.objects.filter(subcategoryid=did).values()
    return JsonResponse(list(product), safe=False)


