from django.shortcuts import render

# Create your views here.

# from django.http import HttpResponse
# from django.template import loader
from django.shortcuts import render
from .models import Fenster
from random import randint

def index(request):
    # template = loader.get_template('fenster/index.bck.html')
    test_creation()
    fenster_list = Fenster.objects.order_by("id")
    context = {
       #  "window_height": 100,
       #  "window_width": fenster_list[0].fenster_width,
       #  "fenstertypes": [True, False],
       #  "how_many_fenster": len(fenster_list),
        "fenster_list": fenster_list,
    }
    # return HttpResponse(template.render(context))
    return render(request, 'fenster/index.bck.html', context)

def test_creation():
# Create a new fenster
    f = Fenster(
        fenster_width=randint(100, 256),
        fenster_height=randint(100, 256),
        window_view=''
    )
    f.save()
