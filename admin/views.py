from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from admin.models import *
from company.models import tbl_company
from guest.models import tbl_login
from shop.models import tbl_shop


# Create your views here.
def home(request):
    return render(request, "admin/home.html")


def districtreg(request):
    if request.method == 'POST':
        districtname = request.POST.get('districtname')
        dist_obj = tbl_district()
        if tbl_district.objects.filter(districtname=districtname).exists():
            return HttpResponse(
                "<script>alert('District Already Exists..');window.location='/Admin/districtreg/';</script>")
        dist_obj.districtname = districtname
        dist_obj.save()
        return HttpResponse("<script>alert('Data Inserted..');window.location='/Admin/districtreg/';</script>")
    return render(request, "admin/district.html")


def locationreg(request):
    if request.method == 'POST':
        locationname = request.POST.get('locationname')
        district = request.POST.get('district')
        emp_obj = tbl_location()
        if tbl_location.objects.filter(locationname=locationname, districtid=district).exists():
            return HttpResponse(
                "<script>alert('Location Already Exists...');window.location='/Admin/locationreg/';</script>")
        emp_obj.districtid = tbl_district.objects.get(districtid=district)
        emp_obj.locationname = locationname
        emp_obj.save()
        return HttpResponse("<script>alert('Location Inserted..');window.location='/Admin/locationreg/';</script>")
    district = tbl_district.objects.all()
    return render(request, "admin/location.html", {'district': district})


def categoryreg(request):
    if request.method == 'POST':
        categoryname = request.POST.get('categoryname')
        categorydesc = request.POST.get('categorydesc')
        cate_obj = tbl_category()
        if tbl_category.objects.filter(categoryname=categoryname).exists():
            return HttpResponse(
                "<script>alert('Category Already Exists..');window.location='/Admin/categoryreg/';</script>")
        cate_obj.categoryname = categoryname
        cate_obj.categorydesc = categorydesc
        cate_obj.categoryphoto = request.FILES['categoryphoto']
        cate_obj.save()
        return HttpResponse("<script>alert('Data Inserted..');window.location='/Admin/categoryreg/';</script>")
    return render(request, "admin/category.html")


def subcategoryreg(request):
    if request.method == 'POST':
        category = request.POST.get('category')
        subcategoryname = request.POST.get('subcategoryname')
        subcategorydesc = request.POST.get('subcategorydesc')
        subcate_obj = tbl_subcategory()
        if tbl_subcategory.objects.filter(subcategoryname=subcategoryname, categoryid=category).exists():
            return HttpResponse(
                "<script>alert('Subcategory Already Exists..');window.location='/Admin/subcategoryreg/';</script>")
        subcate_obj.categoryid = tbl_category.objects.get(categoryid=category)
        subcate_obj.subcategoryname = subcategoryname
        subcate_obj.subcategorydesc = subcategorydesc
        subcate_obj.subcategoryphoto = request.FILES['subcategoryphoto']
        subcate_obj.save()
        return HttpResponse("<script>alert('Data Inserted..');window.location='/Admin/subcategoryreg/';</script>")
    category = tbl_category.objects.all()
    return render(request, "admin/subcategory.html", {'category': category})


def districtview(request):
    emp = tbl_district.objects.all()
    return render(request, "admin/districtview.html", {'district': emp})


def deletedistrict(request, id):
    emp = tbl_district.objects.get(districtid=id)
    emp.delete()
    return districtview(request)


def districtedit(request, id):
    if request.method == 'POST':
        district_name = request.POST.get('districtname')
        emp = tbl_district.objects.get(districtid=id)
        # return HttpResponse(dept_obj)
        emp.districtname = district_name
        emp.save()
        return districtview(request)
    emp = tbl_district.objects.get(districtid=id)
    return render(request, "admin/districtedit.html", {'emp': emp})


def locationview(request):
    district = tbl_district.objects.all()
    emp = tbl_location.objects.all()
    return render(request, "admin/locationview.html", {'location': emp, 'district': district})


def filllocation(request):
    did = int(request.POST.get("did"))
    location = tbl_location.objects.filter(districtid=did).values()
    return JsonResponse(list(location), safe=False)


def deletelocation(request, id):
    emp = tbl_location.objects.get(locationid=id)
    emp.delete()
    return locationview(request)


def locationedit(request, id):
    if request.method == 'POST':
        district = request.POST.get('district')
        location_name = request.POST.get('locationname')
        emp = tbl_location.objects.get(locationid=id)
        # return HttpResponse(dept_obj)
        emp.locationname = location_name
        emp.districtid = tbl_district.objects.get(districtid=district)
        emp.save()
        return locationview(request)
    district = tbl_district.objects.all()
    emp = tbl_location.objects.get(locationid=id)
    return render(request, "admin/locationedit.html", {'emp': emp, 'district': district})


def categoryview(request):
    emp = tbl_category.objects.all()
    return render(request, "admin/categoryview.html", {'category': emp})


def deletecategory(request, id):
    emp = tbl_category.objects.get(categoryid=id)
    emp.delete()
    return categoryview(request)


def categoryedit(request, id):
    if request.method == 'POST':
        category_name = request.POST.get('categoryname')
        category_desc = request.POST.get('categorydesc')
        emp = tbl_category.objects.get(categoryid=id)
        # return HttpResponse(dept_obj)
        emp.categoryname = category_name
        emp.categorydesc = category_desc
        if len(request.FILES) == 0:
            emp.categoryphoto = request.POST.get("photoold")
        else:
            emp.categoryphoto = request.FILES["categoryphoto"]
        emp.save()
        return categoryview(request)
    emp = tbl_category.objects.get(categoryid=id)
    return render(request, "admin/categoryedit.html", {'emp': emp})


def subcategoryview(request):
    category = tbl_category.objects.all()
    emp = tbl_subcategory.objects.all()
    return render(request, "admin/subcategoryview.html", {'subcategory': emp, 'category': category})


def fillsubcategory(request):
    did = int(request.POST.get("did"))
    subcategory = tbl_subcategory.objects.filter(categoryid=did).values()
    return JsonResponse(list(subcategory), safe=False)




def deletesubcategory(request, id):
    emp = tbl_subcategory.objects.get(subcategoryid=id)
    emp.delete()
    return subcategoryview(request)


def subcategoryedit(request, id):
    if request.method == 'POST':
        category = request.POST.get('category')
        subcategory_name = request.POST.get('subcategoryname')
        subcategory_desc = request.POST.get('subcategorydesc')
        emp = tbl_subcategory.objects.get(subcategoryid=id)
        # return HttpResponse(dept_obj)
        emp.subcategoryname = subcategory_name
        emp.subcategorydesc = subcategory_desc
        emp.categoryid = tbl_category.objects.get(categoryid=category)
        if len(request.FILES) == 0:
            emp.subcategoryphoto = request.POST.get("photoold")
        else:
            emp.subcategoryphoto = request.FILES["subcategoryphoto"]
        emp.save()
        return subcategoryview(request)
    category = tbl_category.objects.all()
    emp = tbl_subcategory.objects.get(subcategoryid=id)
    return render(request, "admin/subcategoryedit.html", {'emp': emp, 'category': category})


def shoprequest(request):
    emp = tbl_shop.objects.filter(loginid__status='requested')
    return render(request, "admin/shoprequest.html", {'shop': emp})


def companyrequest(request):
    emp = tbl_company.objects.filter(loginid__status='requested')
    return render(request, "admin/companyrequest.html", {'company': emp})


def shopaccept(request, id):
    login = tbl_login.objects.get(loginid=id)
    login.status = "Accepted"
    login.save()
    return HttpResponse("<script>alert('Shop Accepted..');window.location='/Admin/shopview/';</script>")


def shopreject(request, id):
    login = tbl_login.objects.get(loginid=id)
    login.status = "Rejected"
    login.save()
    return HttpResponse("<script>alert('Shop Rejected..');window.location='/Admin/shopview/';</script>")


def companyaccept(request, id):
    login = tbl_login.objects.get(loginid=id)
    login.status = "Accepted"
    login.save()
    return HttpResponse("<script>alert('Company Accepted..');window.location='/Admin/companyview/';</script>")


def companyreject(request, id):
    login = tbl_login.objects.get(loginid=id)
    login.status = "Rejected"
    login.save()
    return HttpResponse("<script>alert('Company Rejected..');window.location='/Admin/companyview/';</script>")


def shopview(request):
    emp = tbl_shop.objects.filter(loginid__status='Accepted')
    return render(request, "admin/shopview.html", {'shop': emp})


def companyview(request):
    emp = tbl_company.objects.filter(loginid__status='Accepted')
    return render(request, "admin/companyview.html", {'company': emp})
