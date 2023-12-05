from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class TipoPlato(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    codigo = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Productos"


class Plato(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200)
    foto = models.ImageField()
    precio = models.PositiveIntegerField()
    tipo = models.ForeignKey(TipoPlato, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.nombre} - ${self.precio}"


class Sucursal(models.Model):
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=100)
    comuna = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nombre}"

    class Meta:
        verbose_name_plural = "Sucursales"


class Empleado(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    telefono = models.CharField(max_length=100, blank=True, null=True)
    fechaNac = models.DateField(
        blank=True, null=True, verbose_name="Fecha de nacimiento"
    )
    rut = models.CharField(max_length=10, blank=True, null=True)
    sucursal = models.ForeignKey(Sucursal, on_delete=models.PROTECT)


class Mesa(models.Model):
    numero = models.PositiveIntegerField()
    capacidad = models.PositiveIntegerField()
    sucursal = models.ForeignKey(Sucursal, on_delete=models.PROTECT)

    def __str__(self):
        return f"Mesa {self.numero} - {self.sucursal}"
    
class BloqueHorario(models.Model):
    nombre = models.CharField(max_length=50)
    horarioInicio = models.CharField(max_length=50)
    horarioTermino = models.CharField(max_length=50)

class Reserva(models.Model):
    fecha = models.DateField()
    hora = models.TimeField(auto_now_add=True, blank=True)
    personas = models.PositiveIntegerField()
    confirmado = models.BooleanField(default=0)
    mesa = models.ForeignKey(Mesa, on_delete=models.PROTECT)
    usuario = models.ForeignKey(User, on_delete=models.PROTECT)
    bloque = models.ForeignKey(BloqueHorario, on_delete=models.PROTECT)

    def __str__(self):
        return f"Reserva: {self.fecha}"


class Venta(models.Model):
    fecha = models.DateField(auto_now_add=True, blank=True)
    hora = models.TimeField(auto_now_add=True, blank=True)
    sucursal = models.ForeignKey(Sucursal, on_delete=models.PROTECT)
    total = models.PositiveIntegerField()

    def __str__(self):
        return f"Total: ${self.total}"


class DetallePedido(models.Model):
    cantidad = models.PositiveIntegerField()
    venta = models.ForeignKey(Venta, on_delete=models.PROTECT)
    plato = models.ForeignKey(Plato, on_delete=models.PROTECT)


class StockSucursal(models.Model):
    stock = models.PositiveIntegerField()
    sucursal = models.ForeignKey(Sucursal, on_delete=models.PROTECT)
    producto = models.ForeignKey(Producto, on_delete=models.PROTECT)

    class Meta:
        verbose_name_plural = "Stock sucursales"

    def __str__(self):
        return f"Stock Sucursal"    


class CierreCaja(models.Model):
    fecha = models.DateField(auto_now_add=True, blank=True)
    sucursal = models.ForeignKey(Sucursal, on_delete=models.PROTECT)
    total = models.PositiveIntegerField()

    class Meta:
        verbose_name_plural = "Cierre Cajas"
        unique_together = ('fecha', 'sucursal',)

    def save(self, *args, **kwargs):
        ventas = Venta.objects.filter(fecha=self.fecha, sucursal_id=self.sucursal.id)
        total = 0
        for venta in ventas:
            total += venta.total
        self.total = total
        super(CierreCaja, self).save(*args, **kwargs)

    def __str__(self):
        return f"Cierre: {self.fecha}"
