# Generated by Django 4.1.4 on 2023-01-01 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homerent', '0010_meterreadings'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=200)),
                ('last_unit', models.IntegerField()),
                ('new_unit', models.IntegerField()),
                ('tariff', models.DecimalField(decimal_places=3, max_digits=8)),
                ('unit_consumed', models.IntegerField()),
                ('ebill_amt', models.DecimalField(decimal_places=3, max_digits=8)),
                ('rent', models.IntegerField()),
                ('balance', models.DecimalField(decimal_places=3, max_digits=8)),
                ('fine', models.DecimalField(decimal_places=3, max_digits=8)),
                ('total_amount', models.DecimalField(decimal_places=3, max_digits=8)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AlterField(
            model_name='profile',
            name='balance',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='profile',
            name='last_unit',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='profile',
            name='room_no',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='profile',
            name='tarrif',
            field=models.IntegerField(),
        ),
    ]
