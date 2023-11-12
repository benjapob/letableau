from django.shortcuts import render, redirect
from .forms import SignupForm, LoginForm
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
                messages.success(request, f"Bienvenido {username}!")
                return redirect("/")
            else:
                messages.error(request, "Usuario o contraseña incorrectos")
    else:
        form = LoginForm()
    return render(request, "login.html", {"form": form})


def user_logout(request):
    logout(request)
    messages.info(request, "Sesión cerrada correctamente!")
    return redirect("/")


def register(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Cuenta creada exitosamente!")
            return redirect("/")
        else:
            messages.error(request, "Usuario ya existe")
    else:
        form = SignupForm()

    return render(request, "register.html", {"form": form})


def aboutUs(request):
    return render(request, "about-us.html")


def booking(request):
    return render(request, "booking.html")


def contact(request):
    return render(request, "contact.html")
