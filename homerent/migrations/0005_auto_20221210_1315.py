# Generated by Django 3.2.4 on 2022-12-10 13:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homerent', '0004_auto_20221210_1312'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usersdetails',
            name='fullname',
        ),
        migrations.RemoveField(
            model_name='usersdetails',
            name='mobile_number',
        ),
    ]
