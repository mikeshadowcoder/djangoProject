# Generated by Django 4.2.5 on 2023-09-24 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='username',
            field=models.CharField(default=10, max_length=100),
            preserve_default=False,
        ),
    ]
