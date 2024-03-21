# Generated by Django 4.1 on 2024-02-19 09:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('admin', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_location',
            fields=[
                ('locationid', models.AutoField(primary_key=True, serialize=False)),
                ('locationname', models.CharField(max_length=50)),
                ('districtid', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='admin.tbl_district')),
            ],
        ),
    ]
