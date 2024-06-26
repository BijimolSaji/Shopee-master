# Generated by Django 4.1 on 2024-03-08 14:34

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('admin', '0005_tbl_subcategory_categoryid'),
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_unit',
            fields=[
                ('unitid', models.AutoField(primary_key=True, serialize=False)),
                ('unitname', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='tbl_comproduct',
            fields=[
                ('comproductid', models.AutoField(primary_key=True, serialize=False)),
                ('comproductname', models.CharField(max_length=50)),
                ('comproductdesc', models.CharField(max_length=100)),
                ('comprdprice', models.CharField(max_length=50)),
                ('cpyimage1', models.ImageField(upload_to='')),
                ('cpyimage2', models.ImageField(upload_to='')),
                ('regdate', models.DateField(default=datetime.date.today)),
                ('categoryid', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='admin.tbl_category')),
                ('companyid', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='company.tbl_company')),
                ('subcategoryid', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='admin.tbl_subcategory')),
                ('unitid', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='company.tbl_unit')),
            ],
        ),
    ]
