from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.

# from django.http import HttpResponse
# from django.template import loader
from django.shortcuts import render
from .models import Fenster
from .models import Purchase
from random import randint, uniform
import datetime
from decimal import Decimal
from random import randint
from django.contrib.auth.decorators import login_required

def index(request):
    test_creation()
    fenster_list = Fenster.objects.order_by("id")
    context = {
        "request_place": str(request)
    }

    try:
        if 'selected_fenster' in request.POST:
            fenster_id = request.POST['selected_fenster']
            return buy(request, fenster_id)
        context["request_place"] += str(request.POST)
    except Exception as e:
        context["an_axception"] = str(e) + str(type(e))
    return display_all(request, context)

def test_creation():
# Create a new fenster
    f = Fenster(
        fenster_width=randint(100, 256),
        fenster_height=randint(100, 256),
        window_view='',
        fenster_price = Decimal(uniform(0, 5000)),
        for_sale = True
    )
    f.save()

def buy(request, fenster_id):
    all_fensters = Fenster.objects

    purchased_fenster = (Fenster.objects.get(id=fenster_id))
    purchased_fenster.for_sale = False
    purchased_fenster.save()

    purchase = Purchase(
        fenster_id=fenster_id,
        date_time=datetime.datetime.now(),
        price=Decimal(purchased_fenster.fenster_price))
    purchase.save()

    return display_all(request, context)

def display_all(request, context={}):
    context["fenster_list"] = Fenster.objects.filter(for_sale=True).order_by("id")
    purchase_list = Purchase.objects.order_by("id")
    sum = Decimal("0.00")
    for purchase in purchase_list:
        sum += purchase.price
    context["sum"] = sum

    return render(request, 'fenster/index.bck.html', context)   

@login_required
def sell(request):
    if request.method == "POST":
        f = Fenster(
            fenster_width=request.POST['fenster_width'],
            fenster_height=request.POST['fenster_height'],
            fenster_scheme=request.POST['fenster_scheme'],
            window_view='')
        f.save()
    #else:
    return render(request, 'fenster/new.html')

