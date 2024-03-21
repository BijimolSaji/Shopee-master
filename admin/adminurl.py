from django.urls import path
from .import views

urlpatterns=[
    path('home/',views.home),
    path('districtreg/',views.districtreg,name="district"),
    path('locationreg/',views.locationreg,name="location"),
    path('categoryreg/',views.categoryreg,name="category"),
    path('subcategoryreg/',views.subcategoryreg,name="subcategory"),
    path('districtview/',views.districtview),
    path('deletedistrict/<id>/',views.deletedistrict,name="deletedistrict"),
    path('districtedit/<id>/',views.districtedit,name="districtedit"),
    path('locationview/',views.locationview),
    path('filllocation/',views.filllocation,name="filllocation"),
    path('deletelocation/<id>/',views.deletelocation,name="deletelocation"),
    path('locationedit/<id>/',views.locationedit,name="locationedit"),
    path('categoryview/',views.categoryview),
    path('deletecategory/<id>/',views.deletecategory,name="deletecategory"),
    path('categoryedit/<id>/',views.categoryedit,name="categoryedit"),
    path('subcategoryview/',views.subcategoryview),
    path('fillsubcategory/',views.fillsubcategory,name="fillsubcategory"),
    path('deletesubcategory/<id>/',views.deletesubcategory,name="deletesubcategory"),
    path('subcategoryedit/<id>/',views.subcategoryedit,name="subcategoryedit"),
    path('shopview/',views.shopview,name="shopview"),
    path('shoprequestview/',views.shoprequest,name="shoprequestview"),
    path('shopaccept/<id>/',views.shopaccept,name="shopaccept"),
    path('shopreject/<id>/',views.shopreject,name="shopreject"),
    path('companyview/',views.companyview,name="companyview"),
    path('companyrequestview/',views.companyrequest,name="companyrequestview"),
    path('companyaccept/<id>/',views.companyaccept,name="companyaccept"),
    path('companyreject/<id>/',views.companyreject,name="companyreject"),

]