from django.urls import path
from recipes.views import home, contatos, sobre


urlpatterns = [
    path('', home), # Home
    path('sobre/', sobre), # /Sobre
    path('contato/', contatos), # /Contato
]