# Generated by Django 4.2.5 on 2023-09-25 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_remove_employee_job_class'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='name',
            new_name='firstname',
        ),
        migrations.AddField(
            model_name='employee',
            name='city',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='employee',
            name='country',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='employee',
            name='lastname',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
    ]
