from datetime import date

from django.db import models

from admin.models import tbl_location, tbl_category, tbl_subcategory
from guest.models import tbl_login


# Create your models here.

class tbl_company(models.Model):
    companyid = models.AutoField(primary_key=True)
    companyname = models.CharField(max_length=50)
    regno = models.CharField(max_length=50)
    logo = models.ImageField()
    phone = models.BigIntegerField()
    email = models.CharField(max_length=50)
    locationid = models.ForeignKey(tbl_location, on_delete=models.CASCADE, default="")
    loginid = models.ForeignKey(tbl_login, on_delete=models.CASCADE, default="")
    regdate = models.DateField(default=date.today)


class tbl_unit(models.Model):
    unitid = models.AutoField(primary_key=True)
    unitname = models.CharField(max_length=50)


class tbl_comproduct(models.Model):
    comproductid = models.AutoField(primary_key=True)
    companyid = models.ForeignKey(tbl_company, on_delete=models.CASCADE, default="")
    comproductname = models.CharField(max_length=50)
    comproductdesc = models.CharField(max_length=100)
    categoryid = models.ForeignKey(tbl_category, on_delete=models.CASCADE, default="")
    subcategoryid = models.ForeignKey(tbl_subcategory, on_delete=models.CASCADE, default="")
    unitid = models.ForeignKey(tbl_unit, on_delete=models.CASCADE, default="")
    comprdprice = models.IntegerField()
    cpyimage1 = models.ImageField()
    cpyimage2 = models.ImageField()
    regdate = models.DateField(default=date.today)
