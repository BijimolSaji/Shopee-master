from datetime import date

from django.db import models

from admin.models import tbl_location, tbl_category, tbl_subcategory
from company.models import tbl_unit, tbl_comproduct, tbl_company
from guest.models import tbl_login


# Create your models here.
class tbl_shop(models.Model):
    shopid = models.AutoField(primary_key=True)
    shopname = models.CharField(max_length=50)
    ownername = models.CharField(max_length=50)
    phone = models.BigIntegerField()
    email = models.CharField(max_length=50)
    locationid = models.ForeignKey(tbl_location, on_delete=models.CASCADE, default="")
    loginid = models.ForeignKey(tbl_login, on_delete=models.CASCADE, default="")
    regdate = models.DateField(default=date.today)


class tbl_shopproduct(models.Model):
    shopproductid = models.AutoField(primary_key=True)
    shopid = models.ForeignKey(tbl_shop, on_delete=models.CASCADE, default="")
    shopproductname = models.CharField(max_length=50)
    shopproductdesc = models.CharField(max_length=100)
    categoryid = models.ForeignKey(tbl_category, on_delete=models.CASCADE, default="")
    subcategoryid = models.ForeignKey(tbl_subcategory, on_delete=models.CASCADE, default="")
    unitid = models.ForeignKey(tbl_unit, on_delete=models.CASCADE, default="")
    stock = models.IntegerField()
    price = models.IntegerField()
    regdate = models.DateField(default=date.today)


class tbl_cprdrequest(models.Model):
    requestid = models.AutoField(primary_key=True)
    comproductid = models.ForeignKey(tbl_comproduct, on_delete=models.CASCADE, default="")
    companyid = models.ForeignKey(tbl_company, on_delete=models.CASCADE, default="")
    shopid = models.ForeignKey(tbl_shop, on_delete=models.CASCADE, default="")
    unitid = models.ForeignKey(tbl_unit, on_delete=models.CASCADE, default="")
    quantity = models.IntegerField()
    totalprice = models.IntegerField()
    comments = models.CharField(max_length=200)
    status = models.CharField(max_length=50)
    regdate = models.DateField(default=date.today)


class tbl_selectedprd(models.Model):
    selectid = models.AutoField(primary_key=True)
    shopid = models.ForeignKey(tbl_shop, on_delete=models.CASCADE, default="")
    shopproductid = models.ForeignKey(tbl_shopproduct, on_delete=models.CASCADE, default="")
    quantity = models.IntegerField()
    totalprice = models.IntegerField()
    status = models.CharField(max_length=50)


class tbl_salesmaster(models.Model):
    salesid = models.AutoField(primary_key=True)
    shopid = models.ForeignKey(tbl_shop, on_delete=models.CASCADE, default="")
    totalprice = models.IntegerField()
    status = models.CharField(max_length=50)
    salesdate = models.DateField(default=date.today)

class tbl_salesdetails(models.Model):
    salesdetailid = models.AutoField(primary_key=True)
    salesid = models.ForeignKey(tbl_salesmaster, on_delete=models.CASCADE, default="")
    shopproductid = models.ForeignKey(tbl_shopproduct, on_delete=models.CASCADE, default="")
    quantity = models.IntegerField()
    price = models.IntegerField()
    unitid = models.ForeignKey(tbl_unit, on_delete=models.CASCADE, default="")

class tbl_billmaster(models.Model):
    billno = models.AutoField(primary_key=True)
    companyid = models.ForeignKey(tbl_company, on_delete=models.CASCADE, default="")
    shopid = models.ForeignKey(tbl_shop, on_delete=models.CASCADE, default="")
    btotalprice = models.IntegerField()
    dueamount = models.IntegerField()
    status = models.CharField(max_length=50)
    billdate = models.DateField(default=date.today)

class tbl_billdetails(models.Model):
    billdeid = models.AutoField(primary_key=True)
    billno = models.ForeignKey(tbl_billmaster, on_delete=models.CASCADE, default="")
    comproductid = models.ForeignKey(tbl_comproduct, on_delete=models.CASCADE, default="")
    quantity = models.ForeignKey(tbl_cprdrequest, on_delete=models.CASCADE, default="")

