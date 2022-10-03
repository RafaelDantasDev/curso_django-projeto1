from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'recipes/home.html', context={
        'name': 'Rafael'
    })

def contatos(request):
    return HttpResponse('Cotato')

def sobre(request):
    return HttpResponse('Sobre')