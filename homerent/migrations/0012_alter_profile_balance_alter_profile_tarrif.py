# Generated by Django 4.1.4 on 2023-01-01 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homerent', '0011_bills_alter_profile_balance_alter_profile_last_unit_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='balance',
            field=models.DecimalField(decimal_places=3, max_digits=8),
        ),
        migrations.AlterField(
            model_name='profile',
            name='tarrif',
            field=models.DecimalField(decimal_places=3, max_digits=8),
        ),
    ]
