# Generated by Django 4.1.4 on 2023-01-15 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homerent', '0025_profile_contact_no_profile_full_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='contact_no',
            field=models.BigIntegerField(null=True),
        ),
    ]
