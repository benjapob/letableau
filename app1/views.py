from django.shortcuts import render, redirect
from .forms import SignupForm, LoginForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import *
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.


def index(request):
    sucursales = Sucursal.objects.all()
    return render(request, "index.html", {"sucursales": sucursales})


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


def booking(request, id = None, fecha=None, cantidad=None):
    if request.user.is_authenticated:
        if id and fecha and cantidad:
            mesa = Mesa.objects.filter(id = id).get()
            usuario = request.user
            if mesa:
                reserva = Reserva.objects.create(fecha=fecha, personas=cantidad, usuario=usuario, mesa=mesa)
                send_mail(
                subject='Reserva',
                message=("Has reservado una mesa a través de Le Tableau! Aquí están los datos de tu reserva:"+
                "\n\nNombre Completo: "+request.user.first_name+" "+request.user.last_name+
                "\nUsuario: "+request.user.username+
                "\n\nReserva: "+
                "\nFecha de Reserva: "+str(fecha)+
                "\nCantidad de Personas: "+str(cantidad)+
                "\nBloque de Horario: "+'18:00 a 21:00'+
                "\nSucursal: "+mesa.sucursal.nombre+
                "\nDirección sucursal: "+mesa.sucursal.direccion+" - "+mesa.sucursal.comuna+
                "\nMesa reservada: "+str(mesa.numero)+
                "\n\nTe esperamos para que puedas disfutar los mejores platos en nuestras sucursales!"),
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[request.user.email])
                messages.success(request, "Reserva creada exitosamente!")
                return redirect("/")
            else:
                messages.error(request, "Hubo un error al procesar la solicitud")

            
            return render(request, "booking.html")
        else:
            mesas = None
            sucursales = Sucursal.objects.all()
            if request.method == "POST":
                fecha = request.POST.get("fecha")
                cantidad = request.POST.get("cantidad")
                sucursal = request.POST.get("sucursal")
                if (sucursal and fecha and cantidad):
                    reservas = Reserva.objects.filter(fecha = fecha)
                    listaMesas = []
                    for reserva in reservas:
                        listaMesas.append(reserva.mesa.id)
                    mesas = Mesa.objects.filter(sucursal=sucursal, capacidad__gte=cantidad).exclude(id__in=listaMesas)
                    if not mesas:
                        messages.error(request, "No hay mesas disponibles para esa fecha")
                
                else:
                    messages.error(request, "Por favor, ingrese datos válidos")
            

            return render(request, "booking.html", {"mesas": mesas, "sucursales":sucursales, "fecha":fecha, 'cantidad':cantidad})
    else:
        messages.error(request, "Necesitas iniciar sesión para reservar una mesa")
        return redirect("/")



def contact(request):
    return render(request, "contact.html")
