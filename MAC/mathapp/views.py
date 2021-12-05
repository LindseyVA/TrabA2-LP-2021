from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.urls import reverse

def index(request):
    return HttpResponse('<strong>Teste do Matheus na A2</strong>')

def view_dinamica_int(request, param):
    print(param)
    print(type(param))
    if param == 0:
        return HttpResponse('<strong>Paraâmetro 0</strong>')
    elif param == 1:
        return HttpResponse('<strong>Paraâmetro 1</strong>')
    elif param == 2:
        return HttpResponse('<strong>Paraâmetro 2</strong>')
    else:
        raise Http404()

def view_dinamica_str(request, param):
    if param == 'leao':
        return HttpResponse('<strong>Você se acha</strong>')
    else:
        raise Http404()

def matheus(request):
    return render(request, 'mathapp/analise_matheus.html')
