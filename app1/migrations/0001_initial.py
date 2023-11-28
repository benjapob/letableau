# Generated by Django 4.2.4 on 2023-11-28 02:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Mesa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.PositiveIntegerField()),
                ('capacidad', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('codigo', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Productos',
            },
        ),
        migrations.CreateModel(
            name='ReservaHorarios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Sucursal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('direccion', models.CharField(max_length=100)),
                ('comuna', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Sucursales',
            },
        ),
        migrations.CreateModel(
            name='TipoPlato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(auto_now_add=True)),
                ('hora', models.TimeField(auto_now_add=True)),
                ('total', models.PositiveIntegerField()),
                ('sucursal', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app1.sucursal')),
            ],
        ),
        migrations.CreateModel(
            name='StockSucursal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stock', models.PositiveIntegerField()),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app1.producto')),
                ('sucursal', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app1.sucursal')),
            ],
            options={
                'verbose_name_plural': 'Stock sucursales',
            },
        ),
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('hora', models.TimeField(auto_now_add=True)),
                ('personas', models.PositiveIntegerField()),
                ('mesa', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app1.mesa')),
            ],
        ),
        migrations.CreateModel(
            name='Plato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=200)),
                ('foto', models.ImageField(upload_to='')),
                ('precio', models.PositiveIntegerField()),
                ('tipo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app1.tipoplato')),
            ],
        ),
        migrations.AddField(
            model_name='mesa',
            name='sucursal',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app1.sucursal'),
        ),
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telefono', models.CharField(blank=True, max_length=100, null=True)),
                ('fechaNac', models.DateField(blank=True, null=True, verbose_name='Fecha de nacimiento')),
                ('rut', models.CharField(blank=True, max_length=10, null=True)),
                ('sucursal', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app1.sucursal')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='DetallePedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.PositiveIntegerField()),
                ('plato', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app1.plato')),
                ('venta', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app1.venta')),
            ],
        ),
    ]
