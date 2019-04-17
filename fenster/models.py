from django.db import models

# Create your models here

class Fenster(models.Model):
    fenster_width = models.IntegerField()
    fenster_height = models.IntegerField(default=0)
    window_view = models.CharField(
        default ='',
        max_length=1024
    )
