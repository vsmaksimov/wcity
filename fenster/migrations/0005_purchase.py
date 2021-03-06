# Generated by Django 2.1.7 on 2019-04-19 12:57

from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fenster', '0004_fenster_fenster_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fenster_id', models.IntegerField()),
                ('date_time', models.DateTimeField()),
                ('price', models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=10)),
            ],
        ),
    ]
