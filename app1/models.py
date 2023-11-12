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
    precio = models.IntegerField()
    tipo = models.ForeignKey(TipoPlato, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.nombre} - ${self.precio}"


class Sucursal(models.Model):
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=100)
    comuna = models.CharField(max_length=50)

    @classmethod
    def get_default_pk(cls):
        sucursal, created = cls.objects.get_or_create(
            nombre="default sucursal",
            direccion="default direccion",
            comuna="default comuna",
        )
        return sucursal.pk

    def __str__(self):
        return f"{self.nombre}"

    class Meta:
        verbose_name_plural = "Sucursales"


class Empleado(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    telefono = models.CharField(max_length=100, blank=True, null=True)
    fechaNac = models.DateField(blank=True, null=True)
    sucursal = models.ForeignKey(
        Sucursal, on_delete=models.PROTECT, default=Sucursal.get_default_pk
    )


class Mesa(models.Model):
    numero = models.IntegerField()
    capacidad = models.IntegerField()
    reservada = models.BooleanField()
    sucursal = models.ForeignKey(Sucursal, on_delete=models.PROTECT)

    def __str__(self):
        return f"Mesa {self.numero} - {self.sucursal}"


class Reserva(models.Model):
    fecha = models.DateField()
    hora = models.TimeField(auto_now_add=True, blank=True)
    estado = models.CharField(max_length=50)
    mesa = models.ForeignKey(Mesa, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.fecha} - {self.hora} - {self.mesa}"


class Venta(models.Model):
    fecha = models.DateField(auto_now_add=True, blank=True)
    hora = models.TimeField(auto_now_add=True, blank=True)
    sucursal = models.ForeignKey(Sucursal, on_delete=models.PROTECT)
    total = models.IntegerField()

    def __str__(self):
        return f"Total: ${self.total}"


class DetallePedido(models.Model):
    cantidad = models.IntegerField()
    venta = models.ForeignKey(Venta, on_delete=models.PROTECT)
    plato = models.ForeignKey(Plato, on_delete=models.PROTECT)


class StockSucursal(models.Model):
    stock = models.PositiveIntegerField()
    sucursal = models.ForeignKey(Sucursal, on_delete=models.PROTECT)
    producto = models.ForeignKey(Producto, on_delete=models.PROTECT)

    class Meta:
        verbose_name_plural = "Stock sucursales"
