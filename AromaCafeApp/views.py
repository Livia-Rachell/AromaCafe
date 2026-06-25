from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, "AromaCafeApp/index.html")


def cardapio(request):
    return render(request, "AromaCafeApp/cardapio.html")


def contato(request):
    return render(request, "AromaCafeApp/contato.html")
