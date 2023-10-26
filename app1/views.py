from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, "index.html")


def menu(request):
    return render(request, "menu.html")


def login(request):
    return render(request, "login.html")


def register(request):
    return render(request, "register.html")


def aboutUs(request):
    return render(request, "about-us.html")


def booking(request):
    return render(request, "booking.html")


def contact(request):
    return render(request, "letableauTemplate/contact.html")
