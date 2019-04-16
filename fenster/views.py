from django.shortcuts import render

# Create your views here.

# from django.http import HttpResponse
# from django.template import loader
from django.shortcuts import render

def index(request):
    # template = loader.get_template('fenster/index.bck.html')
    context = {
        "window_height": 100,
        "window_width": 50,
        "input_id": "input_id",
        "fenstertypes":[ True, True, False, None, ""]
    }
    # return HttpResponse(template.render(context))
    return render(request, 'fenster/index.bck.html', context)
