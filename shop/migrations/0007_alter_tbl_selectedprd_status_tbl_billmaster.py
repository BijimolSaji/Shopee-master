# Generated by Django 4.1 on 2024-03-21 13:57

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0005_delete_tbl_billmaster'),
        ('shop', '0006_remove_tbl_selectedprd_regdate_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tbl_selectedprd',
            name='status',
            field=models.CharField(max_length=50),
        ),
        migrations.CreateModel(
            name='tbl_billmaster',
            fields=[
                ('billno', models.AutoField(primary_key=True, serialize=False)),
                ('btotalprice', models.IntegerField()),
                ('dueamount', models.IntegerField()),
                ('bstatus', models.CharField(max_length=50)),
                ('billdate', models.DateField(default=datetime.date.today)),
                ('companyid', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='company.tbl_company')),
                ('shopid', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='shop.tbl_shop')),
            ],
        ),
    ]
