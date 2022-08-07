# Generated by Django 3.2 on 2022-05-29 15:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=150, unique=True, verbose_name='Producto')),
                ('descripcion', models.CharField(blank=True, max_length=250, null=True, verbose_name='Descripción de Producto')),
                ('costo_colocacion', models.DecimalField(decimal_places=2, default=0.0, max_digits=9, verbose_name='Descripción de Colocación')),
                ('costo_envio', models.DecimalField(decimal_places=2, default=0.0, max_digits=9, verbose_name='Descripción de Envío')),
                ('otros_costos', models.DecimalField(decimal_places=2, default=0.0, max_digits=9, verbose_name='Otros Costos')),
                ('precio_venta', models.DecimalField(decimal_places=2, default=0.0, max_digits=9, verbose_name='Precio de Venta')),
                ('estado', models.BooleanField(default=True, verbose_name='Estado del Producto')),
                ('fecha_create', models.DateField(default=datetime.datetime.now, verbose_name='Fecha')),
            ],
            options={
                'verbose_name': 'Producto',
                'verbose_name_plural': 'Productos',
                'ordering': ['nombre'],
            },
        ),
    ]
