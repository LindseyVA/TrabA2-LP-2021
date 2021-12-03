from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect, Http404

def home(request):
  return render(request, 'MAC/home.html')

def index(request):
    url_redirecionamento = reverse('home')
    return HttpResponseRedirect(url_redirecionamento)

def search(request):
  return render(request, 'MAC/search.html')

def receitas(request):
  return render(request, 'MAC/receitas.htm')

def produtos(request):
  return render(request, 'MAC/produtos.html')

def minhas_receitas(request):
  return render(request, 'MAC/minhas-receitas.html')

def receita(request, param):
  if param == 'pao':
    return render(request, 'MAC/pao.htm')
  elif param == 'lasanha-de-carne-moida':
    return render(request, 'MAC/lasanha_de_carne_moida.htm')
  elif param == 'fricasse-vegetariano':
    return render(request, 'MAC/fricasse_vegetariano.htm')
  elif param == 'capuccino':
    return render(request, 'MAC/capuccino.html')
  else:
    raise Http404()






