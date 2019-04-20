from django.contrib import admin

# Register your models here.

from .models import Fenster, Purchase

admin.site.register(Fenster)
admin.site.register(Purchase)
