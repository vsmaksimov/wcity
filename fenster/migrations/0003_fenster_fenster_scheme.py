# Generated by Django 2.1.7 on 2019-04-18 15:57

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fenster', '0002_fenster_fenster_height'),
    ]

    operations = [
        migrations.AddField(
            model_name='fenster',
            name='fenster_scheme',
            field=models.CharField(default='1,2', max_length=1024, validators=[django.core.validators.int_list_validator]),
        ),
    ]
