from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    context_dict = {'boldmessage': "Crunchy, creamy, cookie..."}
    return render(request, 'rango/index.html', context=context_dict)


def about(request):
    return HttpResponse("Hello About! <br/> <a href='/rango'>Main</a>")
