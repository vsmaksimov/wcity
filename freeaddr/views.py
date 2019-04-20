from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import FreeAddr
from random import uniform
from decimal import Decimal

def index(request):
    # free_addrs_list = []
    # free_addrs_list.append({'coords': '55.78 37.57', 'address': 'Moscow, Yamskogo polya street, 32'},)
    # free_addrs_list.append({'coords': '55.75 37.61', 'address': 'Moscow, Req Square, 3'}) 
    # free_addrs_list.append({'coords': '55.75 37.59', 'address': 'Moscow, New Arbat street, 8'})
    
    test_creation()
    
    free_addr_list = FreeAddr.objects.order_by("id")

    context = {
        'free_addrs': free_addr_list,
    }
    return render(request, 'freeaddr/index.html', context)

def test_creation():
    free_addr = FreeAddr(
        latitude=uniform(-90, 90),
        longitude=uniform(-180, 180),
        address = "address",
        price = Decimal(str(uniform(0, 5000)))
    )
    free_addr.save()
