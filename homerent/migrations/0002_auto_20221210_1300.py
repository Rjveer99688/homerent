# Generated by Django 3.2.4 on 2022-12-10 13:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homerent', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usersdetails',
            name='amount',
        ),
        migrations.RemoveField(
            model_name='usersdetails',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='usersdetails',
            name='electricunit',
        ),
        migrations.RemoveField(
            model_name='usersdetails',
            name='paidamount',
        ),
        migrations.RemoveField(
            model_name='usersdetails',
            name='username',
        ),
    ]
