# Generated by Django 3.2.4 on 2022-12-10 13:12

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('homerent', '0003_mymodels'),
    ]

    operations = [
        migrations.DeleteModel(
            name='MyModels',
        ),
        migrations.AddField(
            model_name='usersdetails',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usersdetails',
            name='electricunit',
            field=models.IntegerField(default=5, max_length=7),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usersdetails',
            name='paidamount',
            field=models.IntegerField(default=100, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usersdetails',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='usersdetails',
            name='username',
            field=models.CharField(default='ragh', max_length=200),
            preserve_default=False,
        ),
    ]