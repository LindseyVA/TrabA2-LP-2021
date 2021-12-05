from django.shortcuts import render

from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.urls import reverse

def index(request):
    return HttpResponse('<strong>Uma das análises</strong>')

def view_dinamica_str(request, param):
    if param == 'analise':
        return render(request, 'lindseyapp/analise_lindsey.html')
    else:
        raise Http404()
