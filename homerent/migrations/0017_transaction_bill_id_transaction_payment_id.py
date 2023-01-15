# Generated by Django 4.1.4 on 2023-01-02 00:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('homerent', '0016_transaction'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='bill_id',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='homerent.bills'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='transaction',
            name='payment_id',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='homerent.usersdetails'),
            preserve_default=False,
        ),
    ]
