from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.

# from django.http import HttpResponse
# from django.template import loader
from django.shortcuts import render
from .models import Fenster
from random import randint

def index(request):
    # test_creation()
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
        window_view=''
    )
    f.save()

def buy(request, fenster_id):
    all_fensters = Fenster.objects
    Fenster.objects.filter(id=fenster_id).delete()
    return display_all(request)

def display_all(request, context={}):
    context["fenster_list"] = Fenster.objects.order_by("id")
    return render(request, 'fenster/index.bck.html', context)    
