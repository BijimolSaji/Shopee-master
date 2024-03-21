# Generated by Django 4.1 on 2024-02-25 17:58

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('guest', '0001_initial'),
        ('admin', '0005_tbl_subcategory_categoryid'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_shop',
            fields=[
                ('shopid', models.AutoField(primary_key=True, serialize=False)),
                ('shopname', models.CharField(max_length=50)),
                ('ownername', models.CharField(max_length=50)),
                ('phone', models.BigIntegerField()),
                ('email', models.CharField(max_length=50)),
                ('regdate', models.DateField(default=datetime.date.today)),
                ('locationid', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='admin.tbl_location')),
                ('loginid', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='guest.tbl_login')),
            ],
        ),
    ]