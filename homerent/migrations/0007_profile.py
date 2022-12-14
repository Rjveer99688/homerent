# Generated by Django 3.2.4 on 2022-12-11 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homerent', '0006_delete_paymentsdetails'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=200)),
                ('home_no', models.CharField(max_length=10)),
                ('building', models.CharField(max_length=200)),
                ('room_no', models.IntegerField(max_length=7)),
                ('last_unit', models.IntegerField(max_length=7)),
                ('tarrif', models.IntegerField(max_length=7)),
                ('balance', models.IntegerField(max_length=7)),
                ('balance_last_updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
