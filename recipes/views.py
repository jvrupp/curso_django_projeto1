from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'global/home.html', context={'name': 'Joao Victor', 'idade': '21'})


def sobre(request):
    return render(request, 'me-apague/teste.html')


def contato(request):
    return HttpResponse('Contato')
