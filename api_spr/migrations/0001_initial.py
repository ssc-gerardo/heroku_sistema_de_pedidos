# Generated by Django 3.1.5 on 2021-01-18 19:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Almacen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Almacenes',
            },
        ),
        migrations.CreateModel(
            name='Articulo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.IntegerField(unique=True)),
                ('descripcion', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name_plural': 'Articulos',
            },
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('codigo', models.CharField(max_length=100, unique=True)),
                ('foto', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('dreccion', models.CharField(max_length=200)),
                ('tipo_de_cliente', models.CharField(choices=[('NO', 'NOMRAL'), ('PL', 'PLATA'), ('OR', 'ORO'), ('PO', 'PLATINO')], default='NO', max_length=2)),
            ],
            options={
                'verbose_name_plural': 'Clientes',
            },
        ),
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('referncia', models.CharField(max_length=200, unique=True)),
                ('codigo_de_socio', models.CharField(max_length=50)),
                ('detalle_pedido', models.CharField(blank=True, max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Empresas',
            },
        ),
        migrations.CreateModel(
            name='PedidoAlmacen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_pedido', models.DateField(auto_now_add=True)),
                ('fecha_surtido', models.DateField(blank=True, null=True)),
                ('urgente', models.BooleanField(default=False)),
                ('surtido', models.BooleanField(default=False)),
                ('almacen', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api_spr.almacen')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api_spr.cliente')),
            ],
            options={
                'verbose_name_plural': 'Pedidos Almacen',
            },
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('direccion', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name_plural': 'Proeedores',
            },
        ),
        migrations.CreateModel(
            name='Sucursal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('referncia', models.CharField(max_length=200, unique=True)),
                ('codigo', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Almacenes',
            },
        ),
        migrations.CreateModel(
            name='PedidoSucursal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_pedido', models.DateField(auto_now_add=True)),
                ('fecha_surtido', models.DateField(blank=True, null=True)),
                ('urgente', models.BooleanField(default=False)),
                ('surtido', models.BooleanField(default=False)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api_spr.cliente')),
                ('sucursal', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api_spr.sucursal')),
            ],
            options={
                'verbose_name_plural': 'Pedidos Sucursal',
            },
        ),
        migrations.CreateModel(
            name='PedidoEmpresa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_pedido', models.DateField(auto_now_add=True)),
                ('fecha_surtido', models.DateField(blank=True, null=True)),
                ('urgente', models.BooleanField(default=False)),
                ('surtido', models.BooleanField(default=False)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api_spr.cliente')),
                ('empresa', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api_spr.empresa')),
            ],
            options={
                'verbose_name_plural': 'Pedidos Empresa',
            },
        ),
        migrations.CreateModel(
            name='PedidoDetalleSucursal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField(default=1)),
                ('articulo', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='api_spr.articulo')),
                ('pedido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='detalle', to='api_spr.pedidosucursal')),
            ],
            options={
                'verbose_name_plural': 'Detalles de pedido a Sucursal',
            },
        ),
        migrations.CreateModel(
            name='PedidoDetalleEmpresa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField(default=1)),
                ('articulo', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='api_spr.articulo')),
                ('pedido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='detalle', to='api_spr.pedidoempresa')),
            ],
            options={
                'verbose_name_plural': 'Detalles de pedido a Empresa',
            },
        ),
        migrations.CreateModel(
            name='PedidoDetalleAlamcen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField(default=1)),
                ('articulo', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='api_spr.articulo')),
                ('pedido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='detalle', to='api_spr.pedidoalmacen')),
            ],
            options={
                'verbose_name_plural': 'Detalles de pedido a Almacen',
            },
        ),
        migrations.AddField(
            model_name='articulo',
            name='proveedores',
            field=models.ManyToManyField(to='api_spr.Proveedor'),
        ),
    ]
