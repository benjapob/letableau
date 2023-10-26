from django.db import models

# Create your models here.


class Producto(models.Model):
    nombre = models.CharField(max_length=50)


class Mesa(models.Model):
    nombre = models.CharField(max_length=50)


class Cliente(models.Model):
    nombre = models.CharField(max_length=50)


class Reserva(models.Model):
    nombre = models.CharField(max_length=50)


class Sucursal(models.Model):
    nombre = models.CharField(max_length=50)


class Venta(models.Model):
    nombre = models.CharField(max_length=50)


class StockSucursal(models.Model):
    nombre = models.CharField(max_length=50)
