# Generated by Django 4.2.5 on 2023-09-25 04:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_alter_employee_job_class'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='job_class',
        ),
    ]