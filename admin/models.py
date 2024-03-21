from django.db import models

# Create your models here.

class tbl_district(models.Model):
    districtid=models.AutoField(primary_key=True)
    districtname=models.CharField(max_length=50)

class tbl_location(models.Model):
    locationid=models.AutoField(primary_key=True)
    locationname=models.CharField(max_length=50)
    districtid=models.ForeignKey(tbl_district,on_delete=models.CASCADE,default="")

class tbl_category(models.Model):
    categoryid=models.AutoField(primary_key=True)
    categoryname=models.CharField(max_length=50)
    categorydesc = models.CharField(max_length=150)
    categoryphoto = models.ImageField()

class tbl_subcategory(models.Model):
    categoryid = models.ForeignKey(tbl_category, on_delete=models.CASCADE, default="")
    subcategoryid=models.AutoField(primary_key=True)
    subcategoryname=models.CharField(max_length=50)
    subcategorydesc = models.CharField(max_length=150)
    subcategoryphoto = models.ImageField()