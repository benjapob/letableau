from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from .models import Empleado
from .models import *

# Register your models here.


class EmpleadoInline(admin.StackedInline):
    model = Empleado
    can_delete = False
    verbose_name_plural = "empleados"


# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (EmpleadoInline,)


class ProductoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "codigo")


"""@admin.display(ordering='producto_codigo', description='Código')
    def get_code(self, obj):
        return obj.codigo.nombre """


class PlatoAdmin(admin.ModelAdmin):
    pass


class SucursalAdmin(admin.ModelAdmin):
    list_display = ("nombre", "direccion", "comuna")


class MesaAdmin(admin.ModelAdmin):
    list_display = ("numero", "capacidad", "sucursal")

    def get_queryset(self, request):
        if request.user.is_superuser:
            return super().get_queryset(request)
        else:
            return (
                super()
                .get_queryset(request)
                .filter(sucursal=request.user.empleado.sucursal)
            )


class ReservaAdmin(admin.ModelAdmin):
    list_display = ("fecha", "mesa", "usuario", "personas")


class DetalleInline(admin.TabularInline):
    model = DetallePedido


class VentaAdmin(admin.ModelAdmin):
    inlines = [DetalleInline]
    list_display = ("fecha", "hora", "total")
    list_filter = ["sucursal"]
    readonly_fields = ("fecha", "hora")

    def get_queryset(self, request):
        if request.user.is_superuser:
            return super().get_queryset(request)
        else:
            return (
                super()
                .get_queryset(request)
                .filter(sucursal=request.user.empleado.sucursal)
            )


class StockAdmin(admin.ModelAdmin):
    list_display = ("stock", "sucursal", "producto")

    def get_queryset(self, request):
        if request.user.is_superuser:
            return super().get_queryset(request)
        else:
            return (
                super()
                .get_queryset(request)
                .filter(sucursal=request.user.empleado.sucursal)
            )


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Plato, PlatoAdmin)
admin.site.register(Mesa, MesaAdmin)
admin.site.register(Venta, VentaAdmin)
admin.site.register(Sucursal, SucursalAdmin)
admin.site.register(Reserva, ReservaAdmin)
admin.site.register(StockSucursal, StockAdmin)
