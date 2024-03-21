from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

from admin.models import tbl_location, tbl_district
from company.models import tbl_company
from guest.models import *
from shop.models import tbl_shop


# Create your views here.
def home(request):
    return render(request,"guest/home.html")

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if tbl_login.objects.filter(username=username, password=password,status="Accepted").exists():
            loginobj = tbl_login.objects.get(username=username, password=password)
            request.session['uname'] = loginobj.username
            request.session['loginid'] = loginobj.loginid
            role = loginobj.role
            if role == 'admin':
                return redirect('/Admin/home/')
            elif role == 'shop':
                return redirect('/Shop/home/')
            elif role == 'company':
                return redirect('/Company/home/')
            else:
                return HttpResponse(
                    "<script>alert('Not an authorized person');window.location='/Guest/login';</script>")
        else:
            return HttpResponse("<script>alert('Invalid username or password');window.location='/Guest/login';</script>")
            return render(request, "guest/login.html")
    else:
        return render(request,"guest/login.html")

def register(request):
    if request.method == 'POST':
        #return HttpResponse("a")
        username = request.POST.get('username')
        password = request.POST.get('password')
        if tbl_login.objects.filter(username=username).exists():
            return HttpResponse("<script>alert('Username already exist');window.location='/Guest/register/';</script>")
        loginobj = tbl_login()
        loginobj.username = username
        loginobj.password = password
        loginobj.role = 'shop'
        loginobj.status='requested'
        loginobj.save()
        email = request.POST.get('email')
        if tbl_shop.objects.filter(email=email).exists():
            return HttpResponse("<script>alert(' Email Already exist');window.location='/Guest/shopregister/';</script>")
        shopobj = tbl_shop()
        shopobj.shopname = request.POST.get('shopname')
        #return HttpResponse(request.POST.get('studentname'))
        shopobj.ownername = request.POST.get('ownername')
        shopobj.email = request.POST.get('email')
        shopobj.phone = request.POST.get('phone')
        shopobj.locationid = tbl_location.objects.get(locationid=request.POST.get('location'))
        shopobj.loginid = loginobj
        shopobj.save()
        return HttpResponse("<script>alert('Shop Registered Successfully');window.location='/Guest/login/';</script>")
    else:
        district = tbl_district.objects.all()
        return render(request, 'guest/register.html', {'district': district})

def filllocation(request):
    did=int(request.POST.get("did"))
    location=tbl_location.objects.filter(districtid=did).values()
    return JsonResponse(list(location),safe=False)

def comregister(request):
    if request.method == 'POST':
        # return HttpResponse("a")
        username = request.POST.get('username')
        password = request.POST.get('password')
        if tbl_login.objects.filter(username=username).exists():
            return HttpResponse("<script>alert('Username already exist');window.location='/Guest/comregister/';</script>")
        loginobj = tbl_login()
        loginobj.username = username
        loginobj.password = password
        loginobj.role = 'company'
        loginobj.status = 'requested'
        loginobj.save()
        email = request.POST.get('email')
        if tbl_company.objects.filter(email=email).exists():
            return HttpResponse(
                "<script>alert(' Email Already exist');window.location='/Guest/comregister/';</script>")
        comobj = tbl_company()
        comobj.companyname = request.POST.get('companyname')
        # return HttpResponse(request.POST.get('studentname'))
        comobj.regno = request.POST.get('regno')
        comobj.logo = request.FILES['logo']
        comobj.email = request.POST.get('email')
        comobj.phone = request.POST.get('phone')
        comobj.locationid = tbl_location.objects.get(locationid=request.POST.get('location'))
        comobj.loginid = loginobj
        comobj.save()
        return HttpResponse("<script>alert('Company Registered Successfully');window.location='/Guest/login/';</script>")
    else:
        district = tbl_district.objects.all()
        return render(request, 'guest/comregister.html', {'district': district})


