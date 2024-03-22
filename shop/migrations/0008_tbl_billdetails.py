# Generated by Django 4.1 on 2024-03-21 14:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0005_delete_tbl_billmaster'),
        ('shop', '0007_alter_tbl_selectedprd_status_tbl_billmaster'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_billdetails',
            fields=[
                ('billdeid', models.AutoField(primary_key=True, serialize=False)),
                ('billno', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='shop.tbl_billmaster')),
                ('comproductid', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='company.tbl_comproduct')),
                ('quantity', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='shop.tbl_cprdrequest')),
            ],
        ),
    ]
