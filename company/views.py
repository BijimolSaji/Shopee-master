import smtplib
from email.message import EmailMessage

from django.http import JsonResponse, HttpResponse
from django.shortcuts import render

from admin.models import tbl_subcategory, tbl_category
from company.models import tbl_comproduct, tbl_unit, tbl_company
from shop.models import tbl_cprdrequest, tbl_shop


# Create your views here.
def home(request):
    return render(request, "company/home.html")


def comproductreg(request):
    if request.method == 'POST':
        comobj = tbl_comproduct()
        c = request.session.get('loginid')
        comobj.companyid = tbl_company.objects.get(loginid=c)
        comobj.comproductname = request.POST.get('comproductname')
        comobj.comproductdesc = request.POST.get('comproductdesc')
        comobj.comprdprice = request.POST.get('comprdprice')
        comobj.cpyimage1 = request.FILES['image1']
        comobj.cpyimage2 = request.FILES['image2']
        comobj.categoryid = tbl_category.objects.get(categoryid=request.POST.get('category'))
        comobj.subcategoryid = tbl_subcategory.objects.get(subcategoryid=request.POST.get('subcategory'))
        unit = request.POST.get('unit')
        comobj.unitid = tbl_unit.objects.get(unitid=unit)
        comobj.save()
        return HttpResponse(
            "<script>alert('Product Registered Successfully');window.location='/Company/comproductreg/';</script>")
    else:
        category = tbl_category.objects.all()
        unit = tbl_unit.objects.all()
        return render(request, 'company/comproductreg.html', {'category': category, 'unit': unit})


def fillsubcategory(request):
    did = int(request.POST.get("did"))
    subcategory = tbl_subcategory.objects.filter(categoryid=did).values()
    return JsonResponse(list(subcategory), safe=False)


def comproductview(request):
    c = request.session.get('loginid')
    companyid = tbl_company.objects.get(loginid=c)
    emp = tbl_comproduct.objects.filter(companyid=companyid)
    return render(request, "company/comproductview.html", {'comproduct': emp})


def deletecomproduct(request, id):
    emp = tbl_comproduct.objects.get(comproductid=id)
    emp.delete()
    return HttpResponse(
        "<script>alert('Product Deleted Successfully');window.location='/Company/comproductview/';</script>")


def comproductedit(request, id):
    if request.method == 'POST':
        category = request.POST.get('category')
        subcategory = request.POST.get('subcategory')
        unit = request.POST.get('unit')
        comproductname = request.POST.get('comproductname')
        comproductdesc = request.POST.get('comproductdesc')
        comprdprice = request.POST.get('comprdprice')
        emp = tbl_comproduct.objects.get(comproductid=id)
        emp.comproductname = comproductname
        emp.comproductdesc = comproductdesc
        emp.comprdprice = comprdprice
        emp.categoryid = tbl_category.objects.get(categoryid=category)
        emp.subcategoryid = tbl_subcategory.objects.get(subcategoryid=subcategory)

        emp.unitid = tbl_unit.objects.get(unitid=unit)
        if 'image1' in request.FILES:
            emp.cpyimage1 = request.FILES['image1']
        else:
            emp.cpyimage1 = request.POST.get('photoold1')

        if 'image2' in request.FILES:
            emp.cpyimage2 = request.FILES['image2']
        else:
            emp.cpyimage2 = request.POST.get('photoold2')

        emp.save()
        return HttpResponse(
            "<script>alert('Product Edited Successfully');window.location='/Company/comproductview/';</script>")
    category = tbl_category.objects.all()
    unit = tbl_unit.objects.all()
    emp = tbl_comproduct.objects.get(comproductid=id)
    return render(request, "company/comproductedit.html", {'emp': emp, 'category': category, 'unit': unit})


def prdrequest(request):
    c = request.session.get('loginid')
    companyid = tbl_company.objects.get(loginid=c)
    emp = tbl_cprdrequest.objects.filter(status='requested', companyid=companyid)
    return render(request, "company/viewprdrequest.html", {'shoprequest': emp})


def reqaccept(request, id):
    prd = tbl_cprdrequest.objects.get(requestid=id)
    email = prd.shopid.email
    prd.status = "Accepted"
    prd.save()
    msg = EmailMessage()
    msg.set_content('Product Request Accepted')
    msg['Subject'] = "Product request"
    msg['from'] = 'bijimolsaji003@gmail.com'
    msg['To'] = {email}
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login('bijimolsaji003@gmail.com', 'kohedecrdcajlzpl')
        smtp.send_message(msg)
    return HttpResponse("<script>alert('Request Accepted..');window.location='/Company/prdrequestview/';</script>")


def reqreject(request, id):
    prd = tbl_cprdrequest.objects.get(requestid=id)
    email = prd.shopid.email
    prd.status = "Rejected"
    prd.save()
    msg = EmailMessage()
    msg.set_content('Product Request Rejected')
    msg['Subject'] = "Product request"
    msg['from'] = 'bijimolsaji003@gmail.com'
    msg['To'] = {email}
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login('bijimolsaji003@gmail.com', 'kohedecrdcajlzpl')
        smtp.send_message(msg)
    return HttpResponse("<script>alert('Request Rejected..');window.location='/Company/prdrequestview/';</script>")


def prdrequestaccept(request):
    c = request.session.get('loginid')
    companyid = tbl_company.objects.get(loginid=c)
    emp = tbl_cprdrequest.objects.filter(status='Accepted', companyid=companyid).values('shopid',
                                                                                        'shopid__shopname').distinct()
    details = tbl_cprdrequest.objects.filter(status='Accepted', companyid=companyid)

    return render(request, "company/prdreqaccept.html", {'shoprequest': emp, 'details': details})


def filldate(request):
    did = int(request.POST.get("did"))
    date = request.POST.get("date")
    shop_requests = tbl_cprdrequest.objects.filter(shopid=did, regdate=date)
    data = list(shop_requests.values())
    return JsonResponse(data, safe=False)


def viewrequestsbyshop(request):
    shop = request.POST.get("shop")
    date = request.POST.get("date")
    login = request.session.get("loginid")
    company = tbl_company.objects.get(loginid=login)
    comp = company.companyid

    shop_requests = tbl_cprdrequest.objects.filter(shopid=shop, regdate=date, status='Accepted', companyid=comp).values(
        'comproductid',
        'comproductid__comproductname',
        'comproductid__cpyimage1',
        'shopid',
        'shopid__ownername',
        'shopid__shopname', 'shopid__locationid__locationname', 'shopid__locationid__districtid__districtname',
        'shopid__phone', 'quantity', 'totalprice', 'comments', 'regdate'
    )
    data = list(shop_requests.values('comproductid',
                                     'comproductid__comproductname',
                                     'comproductid__cpyimage1',
                                     'shopid',
                                     'shopid__ownername',
                                     'shopid__shopname', 'shopid__locationid__locationname',
                                     'shopid__locationid__districtid__districtname',
                                     'shopid__phone', 'quantity', 'totalprice', 'comments', 'regdate'))

    # return HttpResponse(data)
    return JsonResponse(data, safe=False)


def billgen(request):
    return render(request, "company/billgen.html", )
