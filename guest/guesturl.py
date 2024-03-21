from django.urls import path
from .import views

urlpatterns=[
    path('home/',views.home),
    path('login/',views.login,name="login"),
    path('shopregister/',views.register,name="shopreg"),
    path('filllocation/',views.filllocation,name="filllocation"),
    path('comregister/',views.comregister,name="companyreg"),
]