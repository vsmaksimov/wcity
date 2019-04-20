from django.db import models

# Create your models here.

class FreeAddr(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    address = models.CharField(
        default='',
        max_length=1024
    )
    price = models.DecimalField(
        default="0.00",
        max_digits=10,
        decimal_places=2,
    )
