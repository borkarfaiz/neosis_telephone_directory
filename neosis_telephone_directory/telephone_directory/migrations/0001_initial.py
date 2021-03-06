# Generated by Django 3.0.11 on 2020-12-07 12:00

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('first_name', models.CharField(max_length=255)),
                ('middle_name', models.CharField(blank=True, default='', max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('mobile_number', models.CharField(max_length=10, validators=[django.core.validators.RegexValidator(message='Enter Valid Mobile Number', regex='^[6-9]\\d{9}')])),
                ('landline_number', models.CharField(max_length=12, validators=[django.core.validators.RegexValidator(message='Enter Valid Mobile Number', regex='\\d{5}([- ]?)\\d{6}')])),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
