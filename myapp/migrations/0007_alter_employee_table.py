# Generated by Django 4.2.5 on 2023-09-25 04:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_rename_name_employee_firstname_employee_city_and_more'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='employee',
            table='tblempinfo',
        ),
    ]
