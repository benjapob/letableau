from django.contrib import admin
from .models import *

# Register your models here.


class ProductoAdmin(admin.ModelAdmin):
    list_display = [
        "nombre",
    ]


class MesaAdmin(admin.ModelAdmin):
    list_display = [
        "nombre",
    ]


class ReservaAdmin(admin.ModelAdmin):
    list_display = [
        "nombre",
    ]


class ClienteAdmin(admin.ModelAdmin):
    list_display = [
        "nombre",
    ]


class SucursalAdmin(admin.ModelAdmin):
    list_display = [
        "nombre",
    ]


class VentaAdmin(admin.ModelAdmin):
    list_display = [
        "nombre",
    ]


class StockAdmin(admin.ModelAdmin):
    list_display = [
        "nombre",
    ]


admin.site.register(Producto, ProductoAdmin)
admin.site.register(Mesa, MesaAdmin)
admin.site.register(Venta, VentaAdmin)
admin.site.register(Sucursal, SucursalAdmin)
admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Reserva, ReservaAdmin)
admin.site.register(StockSucursal, StockAdmin)
