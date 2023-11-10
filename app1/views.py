from django.shortcuts import render, redirect
from .forms import UserCreationForm, LoginForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
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


def user_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect("/")
    else:
        form = LoginForm()
    return render(request, "login.html", {"form": form})


def user_logout(request):
    logout(request)
    return redirect("/")


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Cuenta creada exitosamente!")
            return redirect("/")
    else:
        form = UserCreationForm()

    return render(request, "register.html", {"form": form})


def aboutUs(request):
    return render(request, "about-us.html")


def booking(request):
    return render(request, "booking.html")


def contact(request):
    return render(request, "contact.html")
