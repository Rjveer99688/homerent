# Generated by Django 4.1.4 on 2023-01-15 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homerent', '0027_alter_profile_contact_no_alter_profile_full_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='profile_pics'),
        ),
    ]