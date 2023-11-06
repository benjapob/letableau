from django.shortcuts import render
from .models import *

# Create your views here.


def index(request):
    return render(request, "index.html")


def menu(request):
    fondos = Plato.objects.filter(tipo=1)
    vinos = Plato.objects.filter(tipo=2)
    postres = Plato.objects.filter(tipo=3)
    return render(
        request,
        "menu.html",
        {
            "fondos": fondos,
            "vinos": vinos,
            "postres": postres,
        },
    )


def login(request):
    return render(request, "login.html")


def register(request):
    return render(request, "register.html")


def aboutUs(request):
    return render(request, "about-us.html")


def booking(request):
    return render(request, "booking.html")


def contact(request):
    return render(request, "contact.html")
