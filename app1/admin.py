from django.contrib import admin
from .models import *

# Register your models here.


class ProductoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "codigo")


"""@admin.display(ordering='producto_codigo', description='Código')
    def get_code(self, obj):
        return obj.codigo.nombre """


class PlatoAdmin(admin.ModelAdmin):
    pass


class SucursalAdmin(admin.ModelAdmin):
    pass


class MesaAdmin(admin.ModelAdmin):
    pass


class ReservaAdmin(admin.ModelAdmin):
    pass


class VentaAdmin(admin.ModelAdmin):
    pass


class StockAdmin(admin.ModelAdmin):
    pass


admin.site.register(Producto, ProductoAdmin)
admin.site.register(Plato, PlatoAdmin)
admin.site.register(Mesa, MesaAdmin)
admin.site.register(Venta, VentaAdmin)
admin.site.register(Sucursal, SucursalAdmin)
admin.site.register(Reserva, ReservaAdmin)
admin.site.register(StockSucursal, StockAdmin)
