from django.db import models
from django.core.validators import int_list_validator
from decimal import Decimal

# Create your models here

class Apartament(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()

class Fenster(models.Model):
    fenster_width = models.IntegerField()
    fenster_height = models.IntegerField(default=0)
    window_view = models.CharField(
        default ='',
        max_length=1024
    )
    fenster_scheme = models.CharField(
        validators=[int_list_validator],
        default='1,2',
        max_length=1024
    )
    fenster_price = models.DecimalField(
        default=Decimal("0.00"),
        max_digits=10,
        decimal_places=2
    )
    for_sale = models.BooleanField(default=True)
    fenster_apartament = models.ManyToManyField(Apartament)

class Purchase(models.Model):
    fenster_id = models.IntegerField()
    date_time = models.DateTimeField()
    price = models.DecimalField(
        default=Decimal("0.00"),
        max_digits=10,
        decimal_places=2
    )
