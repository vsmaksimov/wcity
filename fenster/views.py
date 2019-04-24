from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import send_mail

# Create your views here.

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import Fenster
from .models import Purchase
from random import randint, uniform
import datetime
from decimal import Decimal
from random import randint
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .pswds import gmail_pass


@login_required
def index(request):
    #test_creation()
    fenster_list = Fenster.objects.order_by("id")
    context = {
        "request_place": str(request)
        }
    try:
        if request.method == "POST":
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
    try:
        all_fensters = Fenster.objects

        purchased_fenster = (Fenster.objects.get(id=fenster_id))
        purchased_fenster.for_sale = False
        purchased_fenster.save()

        purchase = Purchase(
            fenster_id=fenster_id,
            date_time=datetime.datetime.now(),
            price=Decimal(purchased_fenster.fenster_price))
        purchase.save()

        send_mail(
            subject='Fenster was sold',
            message='Fenster was sold.',
            from_email='sbdm472@gmail.com',
            recipient_list=['sbdm472@gmail.com'],
            auth_user="sbdm472@gmail.com",
            auth_password=gmail_pass
        )
    except Exception as e:
        print("Error on server")
    else:
        return HttpResponseRedirect("")

def display_all(request, context={}):
    if "fenster_list" not in context:
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

def apply(request):
    lower_price = Decimal(request.GET.get("lower_price", "1.00"))
    upper_price = Decimal(request.GET.get("upper_price", "150.00"))
    fenster_list = Fenster.objects.filter(fenster_price__gte=lower_price, fenster_price__lte=upper_price)
    context = {"fenster_list": fenster_list}
    return display_all(request, context)
