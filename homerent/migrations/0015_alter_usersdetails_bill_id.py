# Generated by Django 4.1.4 on 2023-01-02 00:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('homerent', '0014_rename_electricunit_usersdetails_bill_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usersdetails',
            name='bill_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homerent.bills'),
        ),
    ]
