from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse('HOME 1')

def contatos(request):
    return HttpResponse('Cotato')

def sobre(request):
    return HttpResponse('Sobre')