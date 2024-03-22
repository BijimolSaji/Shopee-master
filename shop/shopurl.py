from django.urls import path
from .import views

urlpatterns=[
    path('home/',views.home),
    path('comproductview/',views.cproductview),
    path('fillsubcategory/',views.fillsubcategory,name="fillsubcategory"),
    path('fillproduct/', views.fillproduct, name="fillproduct"),
    path('comproductdetails/<id>/',views.cproductdetails,name="cproductdetails"),
    path('productreg/', views.productreg, name="shopproductreg"),
    path('fillsubcategory/', views.fillsubcategory, name="fillsubcategory"),
    path('shopproductview/',views.productview),
    path('deleteshopproduct/<id>/',views.deleteshopproduct,name="deleteshopproduct"),
    path('shopproductedit/<id>/',views.shopproductedit,name="shopproductedit"),
    path('sales/',views.sales),
    path('fillshopproduct/', views.fillshopproduct, name="fillshopproduct"),
    path('salesdetails/<id>/',views.salesdetails,name="salesdetails"),
    path('salesbill/',views.salesbill,name="salesbill"),
    path('deleteselecteditem/<id>/', views.deleteselecteditem, name="deleteselecteditem"),
    path('printbill/',views.printbill,name="printbill"),
]