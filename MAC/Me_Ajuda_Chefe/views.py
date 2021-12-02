from django.shortcuts import render
from django.http import HttpResponse

def index(request):
  return HttpResponse('<h1>Só testando aqui</h1>')


