from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home),
    path('comproductreg/', views.comproductreg, name="comproductreg"),
    path('fillsubcategory/', views.fillsubcategory, name="fillsubcategory"),
    path('comproductview/', views.comproductview),
    path('deletecomproduct/<id>/', views.deletecomproduct, name="deletecomproduct"),
    path('comproductedit/<id>/', views.comproductedit, name="comproductedit"),
    path('prdrequestview/', views.prdrequest, name="prdrequestview"),
    path('reqaccept/<id>/', views.reqaccept, name="reqaccept"),
    path('reqreject/<id>/', views.reqreject, name="reqreject"),
    path('prdrequestaccept/', views.prdrequestaccept, name="prdrequestaccept"),
    path('filldate/', views.filldate, name='filldate'),
    path('viewrequestsbyshop/', views.viewrequestsbyshop, name="viewrequestsbyshop"),
    path('billgen/',views.billgen,name="billgen"),

]
