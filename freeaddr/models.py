from django.db import models

# Create your models here.

class FreeAddr(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    address = models.CharField(
        default='',
        max_length=1024
    )
