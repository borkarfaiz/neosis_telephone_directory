# Generated by Django 3.0.11 on 2020-12-09 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('telephone_directory', '0002_auto_20201208_1801'),
    ]

    operations = [
        migrations.AddField(
            model_name='contacts',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='profile_pic/'),
        ),
    ]