from django.db import models
from django.core.validators import int_list_validator

# Create your models here

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
